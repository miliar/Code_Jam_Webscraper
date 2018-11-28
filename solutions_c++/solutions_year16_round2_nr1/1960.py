#include <iostream>
#include<string.h>
#include<map>

using namespace std;

char str2[2005];

int main(int argc, const char * argv[])
{
   freopen("/Users/sangwoo/Desktop/cpp/cpp/input","r",stdin);
   freopen("/Users/sangwoo/Desktop/cpp/cpp/output","w",stdout);
    
    int tt;
    scanf("%d",&tt);
    
    for(int t=1;t<=tt;t++)
    {
        map<char,int> str;
        int cnt[20] = {0,};
        scanf("%s",str2);
        int len = strlen(str2);
        for(int i=0;i<len;i++)
        {
            str[str2[i]]++;
        }
        cnt[0]+=str['Z'];
        str['E']-=str['Z'];
        str['R']-=str['Z'];
        str['O']-=str['Z'];
        str['Z']-=str['Z'];
        
        cnt[2]+=str['W'];
        str['T']-=str['W'];
        str['O']-=str['W'];
        str['W']-=str['W'];
        
        cnt[4]+=str['U'];
        str['F']-=str['U'];
        str['O']-=str['U'];
        str['R']-=str['U'];
        str['U']-=str['U'];

        cnt[6]+=str['X'];
        str['S']-=str['X'];
        str['I']-=str['X'];
        str['X']-=str['X'];
    
        cnt[8]+=str['G'];
        str['E']-=str['G'];
        str['I']-=str['G'];
        str['H']-=str['G'];
        str['T']-=str['G'];
        str['G']-=str['G'];

        
        cnt[5]+=str['F'];
        str['I']-=str['F'];
        str['V']-=str['F'];
        str['E']-=str['F'];
        str['F']-=str['F'];
        
        cnt[3]+=str['H'];
        str['T']-=str['H'];
        str['R']-=str['H'];
        str['E']-=str['H'];
        str['E']-=str['H'];
        str['H']-=str['H'];
        

        cnt[9]+=str['I'];
        str['N']-=str['I'];
        str['N']-=str['I'];
        str['E']-=str['I'];
        str['I']-=str['I'];
        
        
        cnt[1]+=str['O'];
        str['N']-=str['O'];
        str['E']-=str['O'];
        str['O']-=str['O'];
        
        cnt[7]+=str['S'];
        str['E']-=str['S'];
        str['V']-=str['S'];
        str['E']-=str['S'];
        str['N']-=str['S'];
        
        str['S']-=str['S'];
        
        printf("Case #%d: ",t);
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<cnt[i];j++)printf("%d",i);
        }
        printf("\n");
        
        
    }
    return 0;
}