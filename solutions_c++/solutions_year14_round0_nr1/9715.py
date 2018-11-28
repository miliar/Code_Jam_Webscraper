#include<iostream>
#include<vector>
#include<fstream>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std;

int main()
{
     READ("A-small-attempt0.in");
WRITE("A-small-attempt0.out");
int T,counter=0; cin>>T;
while(T--)
{ counter++;
int n,x; cin>>n;
vector<int>v(16);
for(int i=0;i<4;i++)
    { for(int j=0;j<4;j++)
        {   cin>>x;
            if((i+1)==n)
                v[x-1]++;
        }

    }

cin>>n;
for(int i=0;i<4;i++)
    { for(int j=0;j<4;j++)
        {   cin>>x;
            if((i+1)==n)
                v[x-1]++;
        }

    }

int ones=0,twos=0,temp;
for(int i=0;i<16;i++)
{
  if(v[i]==1)
        ones++;
  else if(v[i]==2)
  {
      temp=i+1;
      twos++;
  }
}

if(ones==8)
    cout<<"Case #"<<counter<<": Volunteer cheated!"<<endl;
    else if(twos>1)
    cout<<"Case #"<<counter<<": Bad magician!"<<endl;
    else

    cout<<"Case #"<<counter<<": "<<temp<<endl;

}
return 0;}
