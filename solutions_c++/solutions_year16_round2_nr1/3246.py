#include<iostream>
#include<algorithm>
#include<fstream>

using namespace std;

   int main() 
	  {
        
        long long int i,j,k,t,p,tt;
        
        
        long long int a[100000];
        
        long long int ct[26];
        
        
        cin>>t;
        
        string s="";
        	ofstream outfile;
  	outfile.open("E:\\codejam\\gcodeout.txt");

        long long int q=1;
        
        
        while(t--)
            {
            p=0;
            
            cin>>s;
            
            for(i=0;i<26;i++)
                ct[i]=0;
                
            for(i=0;i<s.length();i++)
                {
                    ct[s[i]-'A']++;
                }
            
            for(i=0;i<s.length();i++)
                {
                    if(s[i]=='Z')
                       {
                                ct['O'-'A']--; 
                                ct['R'-'A']--;
                                a[p++]=0;
                        }
                    else if(s[i]=='W')
                        {
                        ct['O'-'A']--;
						a[p++]=2;
                    }
                    else if(s[i]=='X')
                        {a[p++]=6;
                        ct['S'-'A']--;
                        ct['I'-'A']--;
                        }
                        else if(s[i]=='U')
                        {
                        	a[p++]=4;
                        	ct['O'-'A']--;
                            ct['F'-'A']--;
                            ct['R'-'A']--;
                    }
                    else if(s[i]=='G')
                        {a[p++]=8;
                        ct['I'-'A']--;
                    }
                }
            
            if(ct['O'-'A']>0)
                {
                    for(i=0;i<ct['O'-'A'];i++)
                        a[p++]=1;
                }
            
            
            if(ct['S'-'A']>0)
                {
                    for(i=0;i<ct['S'-'A'];i++)
                        a[p++]=7;
                }
            
            if(ct['F'-'A']>0)
                {
                    tt=ct['F'-'A'];
                    for(i=0;i<tt;i++)
                    {
                        a[p++]=5; ct['I'-'A']--;
                    }
                }
            if(ct['R'-'A']>0)
                {
                    for(i=0;i<ct['R'-'A'];i++)
                        a[p++]=3;
                }
            
            if(ct['I'-'A']>0)
                {
                    for(i=0;i<ct['I'-'A'];i++)
                        a[p++]=9;
                }
            
			sort(a,a+p);
			
		outfile <<"Case #"<<q++<<":  ";
			
			for(i=0;i<p;i++)
			outfile<< a[i] ;

			
			outfile<<endl;
            
        }
        
        
            
}
