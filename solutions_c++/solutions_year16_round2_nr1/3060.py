#include <cstdio>
#include <vector>
#include <memory.h>
using namespace std;

int a[100];

bool isEmpty()
{
    for(int i='A';i<='Z';++i) if(a[i]>0) return false;
    return true;
}

int main()
{
    char str[2010];
    
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;++i)
    {
        scanf("%s",str);
        printf("Case #%d: ",i);
        memset(a, 0, sizeof(a));
        for(char *ptr=str;*ptr;++ptr) ++a[*ptr];
        vector<int> vec;
        while(!isEmpty())
        {
            if(a['Z']&&a['E']&&a['R']&&a['O'])
            {
                vec.push_back(0);
                --a['Z'];
                --a['E'];
                --a['R'];
                --a['O'];
            }
            else if(a['S']&&a['I']&&a['X'])
            {
                vec.push_back(6);
                --a['S'];
                --a['I'];
                --a['X'];
            }
            else if(a['S']&&a['E']>=2&&a['V']&&a['N'])
            {
                vec.push_back(7);
                --a['S'];
                a['E']-=2;
                --a['V'];
                --a['N'];
            }
            else if(a['F']&&a['I']&&a['V']&&a['E'])
            {
                vec.push_back(5);
                --a['F'];
                --a['I'];
                --a['V'];
                --a['E'];
            }
            else if(a['E']&&a['I']&&a['G']&&a['H']&&a['T'])
            {
                vec.push_back(8);
                --a['E'];
                --a['I'];
                --a['G'];
                --a['H'];
                --a['T'];
            }
            else if(a['T']&&a['H']&&a['R']&&a['E']>=2)
            {
                vec.push_back(3);
                --a['T'];
                --a['H'];
                --a['R'];
                a['E']-=2;
            }
            
            else if(a['T']&&a['W']&&a['O'])
            {
                vec.push_back(2);
                --a['T'];
                --a['W'];
                --a['O'];
            }
            
            else if(a['F']&&a['O']&&a['U']&&a['R'])
            {
                vec.push_back(4);
                --a['F'];
                --a['O'];
                --a['U'];
                --a['R'];
            }
            
            else if(a['O']&&a['N']&&a['E'])
            {
                vec.push_back(1);
                --a['O'];
                --a['N'];
                --a['E'];
            }
            
            else if(a['N']>=2&&a['I']&&a['E'])
            {
                vec.push_back(9);
                a['N']-=2;
                --a['I'];
                --a['E'];
            }
        }
        sort(vec.begin(), vec.end());
        for(vector<int>::iterator it=vec.begin();it!=vec.end();++it)
            printf("%d",*it);
        
        putchar('\n');
        
    }
    
    return 0;
}