#include <bits/stdc++.h>
#include<cstring>
using namespace std;

bool isSame(char *s,int n,bool &c){
	for(int i=0;i<n-1;i++){
		if(s[i]!=s[i+1])
			return false;
	}
	if(s[0]=='-')
		c=false;
	else
		c=true;
	return true;
}

int main()
{
    int t,i=1;
    cin>>t;
    while(i<=t)
    {
        //string str;
        char str[100];
        cin>>str;
        int  n=strlen(str);
        int j=0;
        bool c;
        if(n == 1) 
        {
        if(str[0]=='-')
        cout<<"Case #"<<i<<": 1"<<endl;
        else
        cout<<"Case #"<<i<<": 0"<<endl;
        }
        else if(isSame(str,n,c)){
        	if(c)
            	cout<<"Case #"<<i<<": 0"<<endl;
            else
            	cout<<"Case #"<<i<<": 1"<<endl;
           }
        else
        {
            int ct=0;
            while(true)
            {
                if(str[j] == str[j+1]&&j<n)
                {
                    j++;
                }
                else
                {
                    if(str[j] != str[j+1] && j<n)
                        ct++;
                    for(int k=0; k<=j; k++)
                    {
                        str[k]=str[j+1];
                    }
                    j++;
                }

                if(j==n-1)
                {
                    if(str[j-1]=='-')ct++;
                    cout<<"Case #"<<i<<": "<<ct<<endl;;
                    break;
                }

                

            }

        }

        i++;

    }




    return 0;
}
