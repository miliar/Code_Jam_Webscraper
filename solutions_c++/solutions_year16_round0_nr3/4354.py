#include<bits/stdc++.h>
using namespace std;

bool pr[1000006];
string a[504]={
"1000000000000001 3 2 5 2 7 2 3 2 7 ",
"1000000000000101 13 11 3 4751 173 3 53 109 3 ",
"1000000000000111 3 2 5 2 7 2 3 2 11 ",
"1000000000001001 73 5 3 19 19 3 5 19 3",
"1000000000001101 3 2 5 2 7 2 3 2 11 ",
"1000000000010011 3 2 5 2 7 2 3 2 7 ",
"1000000000011001 3 2 5 2 7 2 3 2 11 ",
"1000000000011011 5 1567 15559 6197 5 5 1031 7 83",
"1000000000011111 3 2 3 2 7 2 3 2 3 ",
"1000000000100101 3 2 5 2 7 2 3 2 7 ",
"1000000000101011 3 7 13 3 5 43 3 73 7 ",
"1000000000101111 5 2 3 2 37 2 5 2 3 ",
"1000000000110001 3 2 5 2 7 2 3 2 11 ",
"1000000000110101 23 17 11 23 5 299699 43 239 59 ",
"1000000000110111 3 2 3 2 7 2 3 2 3 ",
"1000000000111011 17 2 3 2 73 2 17 2 3 ",
"1000000000111101 3 2 3 2 7 2 3 2 3 ",
"1000000001000011 3 2 5 2 7 2 3 2 11 ",
"1000000001011101 17 2 3 2 1297 2 11 2 3 ",
"1000000001011111 59 113 7 157 19 1399 7 43 107",
"1000000001100001 3 2 5 2 7 2 3 2 11 ",
"1000000001100011 23 19 11 105491 5 47 11117 1787 127",
"1000000001100111 3 2 3 2 7 2 3 2 3 ",
"1000000001101011 5 2 3 2 37 2 5 2 3 ",
"1000000001101101 3 2 3 2 7 2 3 2 3 ",
"1000000001110011 3 2 3 2 7 2 3 2 3 ",
"1000000001110101 5 2 3 2 37 2 5 2 3 ",
"1000000001111001 3 2 3 2 7 2 3 2 3 ",
"1000000001111011 31 557 7 19 23 1129 7 5441 241 ",
"1000000001001001 3 2 5 2 7 2 3 2 7 ",
"1000000001001111 3 2 3 2 7 2 3 2 3 ",
"1000000001010101 3 7 13 3 5 17 3 53 7 ",
"1000000001010111 5 2 3 2 37 2 5 2 3 ",
"1000000001011001 11 5 281 101 5 67 5 13 19",
"1000000001011011 3 2 3 2 7 2 3 2 3 ",
"1000000001111101 7 19 43 17 55987 23 7 7 31",
"1000000001111111 3 2 5 2 7 2 3 2 7 ",
"1000000010000011 167 2 11 2 58427 2 23 2 839",
"1000000010000101 3 2 5 2 7 2 3 2 11 ",
"1000000010001001 5 2 7 2 1933 2 29 2 157",
"1000000010010001 3 2 5 2 7 2 3 2 7 ",
"1000000010010111 3 2 3 2 7 2 3 2 3 ",
"1000000010011001 7 1667 179 13 5 11 23 7 311",
"1000000010011011 11 2 3 2 13 2 47 2 3",
"1000000010011101 3 2 3 2 7 2 3 2 3 ",
"1000000010100011 3 1259 421 3 5 8893 3 67 17",
"1000000010100111 5 2 3 2 37 2 5 2 3 ",
"1000000010101001 3 5 13 3 5 43 3 73 7 ",
"1000000010110011 47 2 3 2 11 2 204311 2 3",
"1000000010110101 3 2 3 2 7 2 3 2 3"
};
void prime()
{
    pr[0]=pr[1]=1;
    for(int i=2;i<sqrt(1000006);i++)
    {
        if(!pr[i])
        {
            for(int j=i*2;j<=1000006;j=j+i)
            {
                pr[j]=1;
            }
        }
    }
    return;

}
string val;
void  base( long long int N,int b)
{
     if (N==0)
        return ;

   long long int x = N%b;
     N/=b;
     if (x<0)
        N+=1;

     base(N,b);
     if(x<0)
     {
val+=(x+(b*-1))+'0';

     return;

     }
     else
     {


      val+= x+'0';;
      return;

     }




}
unsigned long long int power(unsigned long long int x, unsigned long long  int y)
{
unsigned long long    int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}
set<string> st;
void solve(string s,int i,int n)
{
    //cout<<s<<endl;
    st.insert(s);
    if(st.size()>1000)
        return;
    string s1,s2;
    if(i==n)
        return;
    s1=s;
    if(s1[i]=='0')
    s1[i]='1';
    else
        s1[i]='0';

    solve(s1,i+1,n);
    solve(s,i+1,n);

    return;
}

int main()
{
    prime();

   //freopen("inp.in","r",stdin);
//freopen("ans.out","w",stdout);
    int t,p=0;
    cin>>t;
    while(t--)
    {

long long int n,m,i,j,k,num=0,ct=0,mx=0;
cin>>n>>m;

cout<<"Case #"<<++p<<": "<<endl;
    long long int low=0,high=10e17,mid;
    string s;
for(i=0;i<n;i++)
{
    if(i==0 || i==n-1)
        s+='1';
    else
        s+='0';
}
 j=0;
 st.clear();
 st.insert(s);
 solve(s,1,n-1);
// cout<<st.size()<<endl;

//cout<<"hi "<<endl;
//cout<<num<<endl;
while(!st.empty())
{

num=0;
s=*st.begin();
//cout<<s<<endl;
st.erase(st.begin());
    for(i=n-1;i>=0;i--)
{
    num+=((s[i]-'0')*power(2,j));
  j++;
}

//cout<<num<<endl;
    if(num%2==0)
    {
        num++;

    }

    if(num<100006)
    {
        if(!pr[num])
        {


            num+=2;
            continue;

        }
    }
    else
    {
        int f=0;
        for(i=2;i<=sqrt(num);i++)
        {
            if(num%i==0)
            {
                f=1;
                break;
            }
        }
        if(f)
        {
            f=0;
        }
        else
        {
            num+=2;
            continue;
        }
    }

base(num,2);


vector<long long int> ans;
//cout<<val<<endl;

long long int nx=0;
for(i=2;i<=10;i++)
{
    nx=0;
    j=0;
        for(k=n-1;k>=0;k--)
        {
            nx+=((s[k]-'0')*power(i,j));
            j++;
        }

        if(nx<1000005)
        {
          //  cout<<i<<"  base   "<<nx<<endl;
            if(pr[nx])
            {
                for(long long int h=2;h<=sqrt(nx);h++)
                {
                    if(nx%h==0)
                    {
                        ans.push_back(h);
                        break;
                    }
                }
            }
            else
            {


                ans.clear();
                break;
            }
        }
        else
        {
            int f=0;
            for(long long int ii=2;ii<=sqrt(nx);ii++)
            {
                if(nx%ii==0)
                {
                    f=1;
                    break;
                }
            }

            if(f)
            {
                ans.clear();
                val.clear();
                break;
            }
            else
            {
              //  cout<<i<<"  "<<nx<<endl;
                 for(long long int h=2;h<=sqrt(nx);h++)
                {
                    if(nx%h==0)
                    {
                        ans.push_back(h);
                        break;
                    }
                }
            }

        }


}

if(ans.size()==9)
{
    if(s[0]=='1' && s[n-1]=='1')
    {


    cout<<s<<" ";


    for(i=0;i<ans.size();i++)
        cout<<ans[i]<<" ";


    ans.clear();
    cout<<endl;
    mx++;

    }
}
if(mx==m)
    break;
val.clear();
num+=2;



}

for(i=0;i<50;i++)
{

       cout<<a[i];
    cout<<endl;
}
val.clear();

}



return 0;
}
