#include<bits/stdc++.h>
using namespace std;
bool rec[10];
bool find()
{
    if(rec[0]&&rec[1]&&rec[2]&&rec[3]&&rec[4]&&rec[5]&&rec[6]&&rec[7]&&rec[8]&&rec[9])
        return true;
    else
        return false;
}

int main()
  {
    int T,i,z; 
    long long int n;
    cin>>T;
    for(int x=1;x<=T;x++)
       {
        for( i=0;i<=9;i++)
            rec[i]=false;
        cin>>n;
        if(n==0)
          cout<<"Case #"<<x<<": "<<"INSOMNIA\n";
        else
          {
            for( z=n;!find();z+=n)
              {
                  long long int temp=z;
                  while(temp)
                    {
                      rec[(temp%10)]=true;
                      temp = temp/10;
 
                    }
              }
           cout<<"Case #"<<x<<": "<<z-n<<"\n";
 
    }
}
return 0;
}