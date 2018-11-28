#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char* argv[])
{
    if (argc != 2)
        return 1;
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1)
        return 2;
    char buf[25005];
    memset(buf, 0, 25005);
    read(fd, buf, 25005);
    char* pbuf = &buf[0];
    unsigned long long valO = 0, valX = 0;
    int place = 15;
    char c;
    bool incompl = false;
    int N = 0;
    while (c = *(pbuf++))
    {
        if (c == 'T')
        {
            valO |= (1<<place);
            valX |= (1<<place);
            --place;
        }
        else if (c == 'O')
        {
            valO |= (1<<place);
            --place;
        }
        else if (c == 'X')
        {
            valX |= (1<<place);
            --place;
        }
        else if (c == '.')
        {
            incompl = true;
            --place;
        }
        else
        {
            continue;
        }
        if (place == -1)
        {
            if (++N > 1)
                printf("\n");
            printf("Case #%d: ", N);
            if ((valO & 0x8888) == 0x8888 ||
                (valO & 0x4444) == 0x4444 ||
                (valO & 0x2222) == 0x2222 ||
                (valO & 0x1111) == 0x1111 ||
                (valO & 0xf000) == 0xf000 ||
                (valO & 0x0f00) == 0x0f00 ||
                (valO & 0x00f0) == 0x00f0 ||
                (valO & 0x000f) == 0x000f ||
                (valO & 0x1248) == 0x1248 ||
                (valO & 0x8421) == 0x8421 )
            {
                printf("O won");
            }
            else
            if ((valX & 0x8888) == 0x8888 ||
                (valX & 0x4444) == 0x4444 ||
                (valX & 0x2222) == 0x2222 ||
                (valX & 0x1111) == 0x1111 ||
                (valX & 0xf000) == 0xf000 ||
                (valX & 0x0f00) == 0x0f00 ||
                (valX & 0x00f0) == 0x00f0 ||
                (valX & 0x000f) == 0x000f ||
                (valX & 0x1248) == 0x1248 ||
                (valX & 0x8421) == 0x8421 )
            {
                printf("X won");
            }
            else
            if (incompl)
            {
                printf("Game has not completed");
            }
            else
            {
                printf("Draw");
            }
            valO = valX = 0;
            place = 15;
            incompl = false;
        }
    }
    close(fd);
    return 0;
}
