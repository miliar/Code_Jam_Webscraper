#include <iostream>
using namespace std;
void output(int i,int a){
	cout<<"Case #"<<i<<": "<<a<<endl;
}
#include <string>

const char digit_pairs[201] = {
  "00010203040506070809"
  "10111213141516171819"
  "20212223242526272829"
  "30313233343536373839"
  "40414243444546474849"
  "50515253545556575859"
  "60616263646566676869"
  "70717273747576777879"
  "80818283848586878889"
  "90919293949596979899"
};


std::string& itostr(int n, std::string& s)
{
    if(n==0)
    {
        s="0";
        return s;
    }

    int sign = -(n<0);
    unsigned int val = (n^sign)-sign;

    int size;
    if(val>=10000)
    {
        if(val>=10000000)
        {
            if(val>=1000000000)
                size=10;
            else if(val>=100000000)
                size=9;
            else 
                size=8;
        }
        else
        {
            if(val>=1000000)
                size=7;
            else if(val>=100000)
                size=6;
            else
                size=5;
        }
    }
    else 
    {
        if(val>=100)
        {
            if(val>=1000)
                size=4;
            else
                size=3;
        }
        else
        {
            if(val>=10)
                size=2;
            else
                size=1;
        }
    }
    size -= sign;
    s.resize(size);
    char* c = &s[0];
    if(sign)
        *c='-';

    c += size-1;
    while(val>=100)
    {
       int pos = val % 100;
       val /= 100;
       *(short*)(c-1)=*(short*)(digit_pairs+2*pos); 
       c-=2;
    }
    while(val>0)
    {
        *c--='0' + (val % 10);
        val /= 10;
    }
    return s;
}

std::string& itostr(unsigned val, std::string& s)
{
    if(val==0)
    {
        s="0";
        return s;
    }

    int size;
    if(val>=10000)
    {
        if(val>=10000000)
        {
            if(val>=1000000000)
                size=10;
            else if(val>=100000000)
                size=9;
            else 
                size=8;
        }
        else
        {
            if(val>=1000000)
                size=7;
            else if(val>=100000)
                size=6;
            else
                size=5;
        }
    }
    else 
    {
        if(val>=100)
        {
            if(val>=1000)
                size=4;
            else
                size=3;
        }
        else
        {
            if(val>=10)
                size=2;
            else
                size=1;
        }
    }

    s.resize(size);
    char* c = &s[size-1];
    while(val>=100)
    {
       int pos = val % 100;
       val /= 100;
       *(short*)(c-1)=*(short*)(digit_pairs+2*pos); 
       c-=2;
    }
    while(val>0)
    {
        *c--='0' + (val % 10);
        val /= 10;
    }
    return s;
}
int main(){
	int t,n[101];
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n[i];
	}
	for(int i=1;i<=t;i++){
		if(n[i]==0){cout<<"Case #"<<i<<": INSOMNIA"<<endl;continue;}
		bool x[10]={false},success=false;
		int tmp=0,nn,mm;
		while(tmp<100000 && !success){
			tmp++;
			mm=nn=n[i]*tmp;
			while (nn != 0)
			{
			    int thisDigit = nn % 10;    // Always equal to the last digit of thisNumber
			    int thisNumber = nn / 10;   // Always equal to thisNumber with the last digit chopped off, or 0 if thisNumber is less than 10
			    x[thisDigit]=true;
			    if(x[0]&&x[1]&&x[2]&&x[3]&&x[4]&&x[5]&&x[6]&&x[7]&&x[8]&&x[9]){success=true;output(i,mm);break;}
			    nn /= 10;
			}
		}
		if(!success){cout<<"Case #"<<i<<": INSOMNIA"<<endl;}
	}
	return 0;
}

