#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;
bool pri[1000000];
int ne[10];
long long int fact(long long int a)
{
    for(long long int i=2;i<=sqrt(a);i++)
    {
        if(a%i==0)
            return i;
    }
}
int Sie(long long int a)
{
    // Create a boolean array "prime[0..n]" and initialize
    // all entries it as true. A value in prime[i] will
    // finally be false if i is Not a prime, else true.
    //bool prime[n+1];
    //memset(pri, true, sizeof(pri));
    if(a==0)
        return 0;
    for (long long int p=2; p*p<=a; p++)
    {
        // If prime[p] is not changed, then it is a prime
        //if (pri[p] == true)
        //{
            // Update all multiples of p
          //  for (int i=p*2; i<=1000000; i += p)
          if(a%p==0)
            return 0;
                //pri[i] = false;

    }
    return 1;

    // Print all prime numbers
    //for (int p=2; p<=n; p++)
      // if (prime[p])
        //  cout << p << " ";
}

int fin(long long int s)
{
    long long int ty=s,su,n;
    //cout<<ty<<" ";
    int rem;
    memset(ne,0,sizeof(ne));int k=2;
    for(int i=2;i<=10;i++)
    {
        su=0;ty=s;
        rem=ty%10;
        su+=(rem*1);
        ty/=10;
        n=1;
        while(ty!=0)
        {
            rem=ty%10;
            n=n*i;
            su+=(rem*n);//cout<<su<<" ";
            ty/=10;
        }
        //cout<<"sum"<<s<<" "<<su<<endl;
        //cout<<"k"<<k<<" "<<su<<" "<<" ";
        if(Sie(su)==0)
        {

            ne[k++]=fact(su);
            //cout<<ne[k-1]<<endl;
        }
        else
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    freopen("C-small-attempt2.in","rt",stdin);
	freopen("out1.out","wt",stdout);
    //cout << "Hello world!" << endl;

    //cout<<"jk";
    //char *s="1000010101";
    //long long int ty=atoi(s);
    //cout<<ty;
    int t,uy,ikl;
    cin>>t;
    cin>>uy>>ikl;
    for(int hg=1;hg<=t;hg++){
    cout<<"Case #"<<hg<<":"<<endl;
    int n=uy;int cnt=0;
    for(int i = pow(2,n)/2; i < pow(2,n); i++)
        {
            //cnt++;
            //cout<<cnt;
             string B = "";
            int temp = i;
            for (int j = 0; j < n; j++)
            {
                if (temp%2 == 1)
                    B = '1'+B;
                else
                    B = '0'+B;
                    temp = temp/2;
            }
            //std::string str = "string";
            char *cstr = new char[B.length() + 1];
            strcpy(cstr, B.c_str());
            //char *p=B.c_str();
            long long int ty=atoll(cstr);
            //cout<<endl;
            //cout<<ty<<endl;
            //cout<<ty<<" ";
            if(ty%10==1){
            int jk=fin(ty);
            //cout<<"jk"<<jk;
            //break;
            if(jk==1)
            {
                cout<<ty<<" ";
                for(int io=2;io<=10;io++)
                    cout<<ne[io]<<" ";
                //print array
                cnt++;
                cout<<endl;
            }

            if(cnt==ikl)
                break;
            }

         }
    }
    return 0;
}
