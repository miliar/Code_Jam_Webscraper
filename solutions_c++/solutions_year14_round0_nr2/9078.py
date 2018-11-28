#include<iostream>  
#include<iomanip>
#include<cstdio>  
#include<fstream>  
using namespace std;  

double C, F, X, coo;  

bool doing()  //JUDGE>>>>>>>>>
{  
    double temp = (C/coo) + (X/(coo+F));  
    if(X/coo > temp)  
        return 1;  
    else  
        return 0;  
}  
int main()  
{  
	freopen("B-large.in","r",stdin);
   freopen("output.in","w",stdout);  
    int CaseNum;  
    cin>>CaseNum;  
    for(int idata = 1; idata <= CaseNum; idata++)  
    {  
        coo= 2.0;  
        double result = 0;  
        cin>>C>>F>>X; 
		//while(doing(C,F,X,coo))
        while(doing())  
        {  
            result += C/coo;  
            coo += F;  
        }  

        result += X/coo;  
		cout<<"Case #"<<setiosflags(ios::fixed)<<setprecision(7)<<idata<<": "<<result<<endl;  
    }  
	//system("PAUSE");
    return 0;  
}  