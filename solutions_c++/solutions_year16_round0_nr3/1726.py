#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int total=500;
void findans(string s,int l)
{
    if(total<=0)
        return;
    if(s.size()<l)
    {
        findans(s+"00",l);
        findans(s+"11",l);
    }
    else
    {
        cout<<s<<"1";
        printf(" 3 4 5 6 7 8 9 10 11\n");
        total--;
    }

}
int main()
{
    freopen("QC.out","w",stdout);
    int p=32;
    printf("Case #1:\n");
    findans("1",p-1);
}
