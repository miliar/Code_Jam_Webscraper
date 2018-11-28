#include<cstdio>
#include<string>
using namespace std;

typedef long long LL;

int d,n;
string text;
char tmp[200];

string czytaj()
{
    scanf("%s",tmp);
    return tmp;
}

int main() 
{
    scanf("%d",&d);
    for(int i=1;i<=d;i++)
    {
        string dane = czytaj();
        int kroki = 0;
        bool flipped = 0;
        for(int i2=dane.length()-1;i2>=0;i2--)
        {
            if(dane[i2] == '-' ^ flipped)
            {
                kroki++;
                flipped = !flipped;
            }
        }
        
        
        
        printf("Case #%d: %d\n", i, kroki);
    }
    return 0;
}

