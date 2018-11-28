#include<bits/stdc++.h>
#define SIZE(arr) sizeof(arr) / sizeof(*arr)
using namespace std;
int pinput(char* input, size_t size, size_t cr);
void sfaces(char* input, int l, int h);
int eface(char* input, size_t size);
int main()
{
	freopen("B-large.in","rt",stdin);
    freopen("2-large.out","wt",stdout);
	int t, c = 1,output;
    scanf("%d", &t);
    char input[101];
    while (t--)
    {
        scanf("%s", input);
        output = pinput(input, SIZE(input), 0);
		printf("Case #%d: %d\n", c, output);
	   c++;
    }
    return 0;
}
int pinput(char* input, size_t size, size_t cr)
{
    int index = eface(input, size);
    if(index == -1) return cr;
    sfaces(input, 0, index);
    return pinput(input, index, cr + 1);
}
void sfaces(char* input, int l, int h)
{
    for(int i = l; i <= h; ++i)
        input[i] = input[i] == '+' ? '-' : '+';
}
int eface(char* input, size_t size)
{
    int i;
    for (i = size - 1; i >= 0; i--)
    {
        if(input[i] == '-')
            break;
    }
    return i;
}
