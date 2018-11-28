#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int l=1;l<=t;l++)
    {
       int x,r,c;
       cin>>x>>r>>c;
       if(x==1) printf("Case #%d: GABRIEL\n",l);
       else if((x==2) && (r*c)%2==0 && (r>=2 || c>=2))
       printf("Case #%d: GABRIEL\n",l);
       else if((x==3) && (r*c)%3==0 && (r>=3 || c>=3) && (r>1 && c>1))
       printf("Case #%d: GABRIEL\n",l);
       else if((x==4) && (r*c)%4==0 &&(r>=4 || c>=4) && (r>2 && c>2))
       printf("Case #%d: GABRIEL\n",l);
       else printf("Case #%d: RICHARD\n",l);

    }

    return 0;
}
