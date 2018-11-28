#include<bits/stdc++.h>
using namespace std;
int main()
{
  int l,t,i,cnt,j,ans;
  char str[109];
  cin >> t;
  for(i=1;i<=t;i++)
  { cin >> str;cnt=0;
    l=strlen(str);
    for(j=0;j<l;j++)
    { if(j==0 && str[j]=='-')
        { while(str[j]=='-')
            j++;
          j--;cnt++;
        }
        else if(str[j]=='-')
           { while(str[j]=='-')
               j++;
             j--;
             cnt+=2;

            }

    }



    printf("Case #%d: %d\n",i,cnt);
  }
  return 0;
}
