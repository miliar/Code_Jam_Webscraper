#include <fstream>
#include <string>

std::ifstream INPUT;
std::ofstream OUTPUT;

void RunCase();

int main(int argc, char *argv[])
{
    std::string inFileName("test.in");
    std::string outFileName("test.out");
    if (argc == 3)
    {
        inFileName = argv[1];
        outFileName = argv[2];
    }
    INPUT.open(inFileName.c_str());
    OUTPUT.open(outFileName.c_str());
    int noCases;
    INPUT >> noCases;
    for (int i = 0; i < noCases; i++)
    {
        OUTPUT << "Case #" << i + 1 << ": ";
        RunCase();
        OUTPUT << std::endl;
    }
    INPUT.close();
    OUTPUT.close();
    return 0;
}

#include <vector>
std::vector<std::vector<char> > array;
void ReadArray(int height, int width)
{
    array.resize(height);
    for (int y = 0; y < height; y++)
    {
        array[y].resize(width);
        for (int x = 0; x < width; x++)
            INPUT >> array[y][x];
    }
}

void RunCase()
{
    int h, w;
    INPUT >> h >> w;
    ReadArray(h, w);

    bool can(true);
    for (int y = 0; y < h; y++)
        for (int x = 0; x < w; x++)
        {
            can = true;
            for (int i = 0; i < w; i++)
                if (array[y][x] < array[y][i])
                {
                    can = false;
                    break;
                }
            if (!can)
                for (int i = 0; i < h; i++)
                    if (array[y][x] < array[i][x])
                    {
                        OUTPUT << "NO";
                        return;
                    }
        }
    OUTPUT << "YES";
}
