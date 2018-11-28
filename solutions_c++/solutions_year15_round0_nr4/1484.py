#include<bits/stdc++.h>

#define llu unsigned long long
#define ll long long
#define pi 3.141592
#define nl printf("\n")
#define f(i,l1,l2) for(i=l1;i<l2;i++)
#define gc getchar_unlocked
#define vi vector<int>
#define vit vi::iterator
#define all(c) c.begin(), c.end()
#define pb push_back
using namespace std;

/*void fin(int &x)       //does not compile in codeblocks but does in online judges
{                        //use if input too large ( only for integers )
int i=0;x=0;
register int c=gc();
while(c<48||c>57)
c=gc();
while(c>47&&c<58)
{
x=(x<<1)+(x<<3) + c-48;
i++;
c=gc();
}
}*/

int main()
{
    int t,i,n,j=1;
    cin>>t;
    while(t--)
    {
        int x,r,c;
        cin>>x>>r>>c;
        if(x==1) // all possible
        {
            cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
            j++;
        }

        if(x==2)
        {
            //over spilling ot overlap
            if((r==1&&c==1)||(r==1&&c==3)||(c==1&&r==3)||(r==3&&c==3))
            {
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
                j++;
            }
            else
            {
                cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
                j++;
            }
        }

        if(x==3)
        {
            //over spilling ot overlap //for or -- > see shape
            if((r==1||c==1)||(r==2&&c==2)||(r==2&&c==4)||(r==4&&c==2)||(r==4&&c==4))
            {
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
                j++;
            }
            else
            {
                cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
                j++;
            }
        }

        if(x==4)
        {

            if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4)) // win in these
            {
                cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
                j++;
            }
            else //over spilling ot overlap //for or -- > see shape
            {
                cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
                j++;
            }
        }
}


    return 0;
}

