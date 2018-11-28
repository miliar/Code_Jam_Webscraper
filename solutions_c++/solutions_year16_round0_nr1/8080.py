#include <iostream>
#include <stdio.h>
#include <set>
using namespace std;
void int2dig(int x, set<int> &l)
{
    int y = 10;
    while(x>=y)
    {
        l.insert(x%y);
        x-=x%y;
        x=x/10;
    }
    l.insert(x);
}
void print_set(set<int> l)
{
    set<int>::iterator iter;
    for(iter=l.begin(); iter!=l.end();++iter)
        cout<<(*iter)<<endl;
}
int main()
{
    int t,n,tmp,c;
    set<int> digits;
    FILE * pFile;
    FILE * rFile;
    bool isAsleep;
    pFile = fopen ("A-large.in","r");
    rFile = fopen ("A-small-practice.out","w+");
    fscanf (pFile, "%d",&t);
    for(int i = 0; i<t;i++)
    {
        fscanf (pFile, "%d",&n);
        if (n==0)
        {
            fprintf(rFile, "Case #%d: INSOMNIA\n", i+1);
        }
        else
        {
            isAsleep = false;
            tmp = n;
            c = 2;
            int2dig(n, digits);
            while (!isAsleep)
            {
                if(digits.count(0)==1&&digits.count(1)==1&&digits.count(2)==1&&digits.count(3)==1&&digits.count(4)==1&&digits.count(5)==1&&digits.count(6)==1&&digits.count(7)==1&&digits.count(8)==1&&digits.count(9)==1)
                {
                    isAsleep = true;
                    fprintf(rFile, "Case #%d: %d\n", i+1, tmp);
                }
                else
                {
                    tmp = n*c;
                    int2dig(tmp, digits);
                    c++;
                }
            }
            digits.clear();
        }
    }
    fclose (pFile);
    fclose (rFile);
    return 0;
}
