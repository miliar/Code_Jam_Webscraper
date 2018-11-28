#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    freopen("C:\\Users\\Balasubramanian\\Downloads\\A-small-attempt1.in.", "r", stdin);
    freopen("C:\\Users\\Balasubramanian\\Desktop\\C++progs\\output12.out", "w", stdout);
    int t;scanf("%d",&t);int c=0;
    while(t--){c++;
    int r1;scanf("%d",&r1);
    int a[4][4];
    for(int i=0;i<4;++i)for(int j=0;j<4;++j)
    scanf("%d",&a[i][j]);
    vector<int> v1;
    for(int i=0;i<4;++i)
    v1.push_back(a[r1-1][i]);
    int r2;scanf("%d",&r2);
    int a2[4][4];
    for(int i=0;i<4;++i)for(int j=0;j<4;++j)
    scanf("%d",&a2[i][j]);
    vector<int> v2;
    for(int i=0;i<4;++i)
    v2.push_back(a2[r2-1][i]);
    int count=0,ans=0;
    for(int i=0;i<v1.size();++i)
    {
        for(int j=0;j<v2.size();++j)
        if(v1[i]==v2[j])
        {
            count++;ans=v1[i];
        }
    }
    string s;
    if(count==1)
    {
        
      printf("Case #%d: %d\n", c, ans);
    }
    else if(count==0)
    {
        s="Volunteer cheated!";
        printf("Case #%d: %s\n", c, s.c_str());
    }
    
     else if(count>1)
    {
        s="Bad magician!";
        printf("Case #%d: %s\n", c, s.c_str());
    }
    
    
    }
    
    
    
    
    return 0;
}
