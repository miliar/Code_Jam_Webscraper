#include<fstream>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
bool sqrot(  int64_t n,  int64_t* sqrt)
{
    *sqrt=1;
    while (n>=(*sqrt+1)*(*sqrt+1) || n<(*sqrt)*(*sqrt))
    {
        *sqrt=(*sqrt+(n/(*sqrt)))/2;
    }
    return((*sqrt)*(*sqrt)==n);
};
bool palindrome(  int64_t x)
{
      int64_t temp=x;  int64_t rev=0;
    while (temp>=1)
    {
        rev=(rev*10)+(temp%10);
        temp/=10;
    }
    return((x==rev));
};
int main()
{
  int64_t T,N,M;
  int64_t x;
  int64_t sqroot=1;
char str[30];
cin>>str;
fstream fi,fo;
fi.open(str,fstream::in);
fo.open("output.txt",fstream::out);
fi>>T;
  int64_t count;
  int64_t first;
  int64_t last;
for (int64_t k=0;k<T;k++)
{
    count=0;
    fi>>first;
    fi>>last;
    for(int64_t i=first;i<=last;i++)
    {
            if(palindrome(i)&&sqrot(i,&sqroot))
            {
                if(palindrome(sqroot)){count++;}
            }
    }
    fo<<"Case #"<<k+1<<": "<<count<<endl;
}
fi.close();
fo.close();
return (0);
}
