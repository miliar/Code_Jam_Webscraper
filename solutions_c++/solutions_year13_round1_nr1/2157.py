#include<iostream>
#include<stdio.h>

using namespace std;

long long ans,s_n,f_n,t,b; 
long long i,j,k,p,q,z;//iteratr
int c1,c2,f,f1,f2;//counter
char ch;
double r,tot;
double sol;
double area,startArea,endArea;
int flag;
double returnArea(long long n,long long r)
{
    sol = 2*n*r + n*(2*n - 1);
    return sol;
}
int calc()
{    
    flag = 0;
    area = 0;
    i = 1;
    s_n = 1;
    f_n = 100;
    ///*
    while(flag == 0)
    {
        //cout << "s_n " << s_n << endl;
        //cout << "f_n " << f_n << endl;
        startArea = returnArea(s_n,r);
        endArea = returnArea(f_n,r);
        if(tot >= startArea && tot <= endArea)
        {
            flag = 1;
        }
        else if(tot < startArea)
        {
            f_n = s_n - 1;
            s_n = s_n/2;           
        }
        else if(tot > endArea)
        {
            s_n = f_n + 1;
            f_n = 2 * f_n;
        }
    }
    //*/
    //for(i = s_n;i < f_n; i++)
    i = s_n;
    while(true)
    {
        //cout<< "i:"<< i<<endl;        
        startArea = returnArea(i,r);
        endArea = returnArea((i+1),r);        
        if(tot >= startArea && tot < endArea)
        {
            //cout << "s " << startArea << endl;
            //cout << "e " << endArea << endl;            
            return i;
        }
        i++;
    }
    return 0;
}

int main(){
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;	
    k = 1;
    while(k<=t)
    {        
        tot = 0;
        cin >> r >> tot;        
        ans = calc();
		cout << "Case #"<<k<<": "<< ans << endl;        
        k++;
    }	
    return 0;
}
