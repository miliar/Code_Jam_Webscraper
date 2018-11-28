

#include <iostream>
#include <stdio.h>
#include <string>
#include <map>

using namespace std;
int data[100][100];
int n;


int main(int argc, const char * argv[]) {
   freopen("/Users/sangwoo/Desktop/cpp/cpp/input","r",stdin);
   freopen("/Users/sangwoo/Desktop/cpp/cpp/output","w",stdout);
    
    int tt;
    
    cin >> tt;
    for(int t=1;t<=tt;t++)
    {
        map<int , int>cnt;
        
        scanf("%d",&n);
        for(int i=0;i<n*2-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                int a;
                scanf("%d",&a);
                cnt[a]++;
                
            }
        }
        printf("Case #%d: ",t);
        for(auto it = cnt.begin() ; it != cnt.end(); it++)
        {
            if((it)->second%2 == 1)
            {
                printf("%d ",it->first);
            }
        }
        printf("\n");
    }
    
    
    

    return 0;
}