    #include <iostream>
    #include <string>
    #include <stdlib.h>
    #include <fstream>
    #include <vector>
    #include <algorithm>
	#include <stdio.h>
	#include <stdlib.h>
using namespace std;
	int main()
	{	
		ifstream infile("A.in");
		ofstream outfile("Asmall.out");
		string temp;string::size_type sz=0;
		getline(infile,temp);
		int testcases ;
		testcases=stoi(temp,&sz,10);
		sz=0;		
		int cou=0;
		int Smax ; string Si;
		int number=0,countup=0,countzero=0;;
		while(cou<testcases)
		{
			number=0;
			getline(infile,temp);
			Smax=stoi(temp,&sz,10);
			temp=temp.substr(sz+1);
			Si=temp;			
			for(int i=0;i<Si.size();i++)
			{
				if(Si.at(i)=='0')
					continue;
				if(countup<i)
				{
					number+=(i-countup);
					countup+=(i-countup);
				}
				countup+=(Si.at(i)-48);					
			}			
			countup=0;
			outfile<<"Case #"<<cou+1<<": "<<number<<endl;

			cou++;
		}
		system("pause");
		return 0;
	}

	

	/*

	ifstream infile("A.in");
		ofstream outfile("hesham.txt");
		int testcases;	string temp;string::size_type sz=0;
		getline(infile,temp);
		testcases=stoi(temp,&sz,10);
		sz=0;
		int cou=0;
		int x;int *arr,*arr2;int counter=0;
		while(cou<testcases)
		{
		counter =0;
		getline(infile,temp);
		x=stoi(temp,&sz,10);
		sz=0;
		arr=new int[x];
		arr2=new int [x];
		for (int i=0;i<x;i++)
		{	
			getline(infile,temp);
			arr[i]=stoi(temp,&sz,10);
			temp=temp.substr(sz);
			arr2[i]=stoi(temp,&sz,10);
			sz=0;
		}
		for (int i=0;i<x;i++)
		{
			for (int j=0;j<x;j++)
			{
				if (i==j){continue;}
			if (arr[i]>arr[j] && arr2[i]<=arr2[j] || arr[i]<arr[j] && arr2[i]>=arr2[j])
                counter++;
           if (arr[i]>=arr[j] && arr2[i]<arr2[j] || arr[i]<=arr[j] && arr2[i]>arr2[j])
                counter++;
       }
   }
		outfile<<"Case #"<<cou+1<<": "<<counter/4<<endl;
	cou++;
		}
		*/
  /*  void rot(char **x,int siz);
    void grav(char **x,int siz);
    int main()
    {
        ifstream infile("A-large-practice.in");
        ofstream outfile("answers.txt");
        string you;

        int testcases; int cR=0,cB=0;
        bool checkR=false,checkB=false;
        getline(infile,you);
        string::size_type sz=0;
        testcases = stoi(you,&sz,10);
        
        //cin>>testcases;
        int N ,K ;//int arr[2];int z=0;
        int cou=0;
		string::size_type sz2=0;
		
        while(cou<testcases)
        {	//string you2="";
            //getline(infile,you);
            while(!you.empty())
		{	
			getline(infile,you);
			N=stoi(you,&sz2,10);
			you=you.substr(sz2);
			K=stoi(you,&sz2,10);
			you=you.substr(sz2);
		}	
			//cin>>N>>K;
			sz2=0;
            char **v = new char *[N];
			//char *temp=new char[N];
			//std::streamsize c=N;
        for(int i=0;i<N;i++)
        {
            v[i]=new char[N];
        }
            for(int i=0;i<N;i++)
            {   
				getline(infile,you);
                for(int j=0;j<N;j++)
                {
                    v[i][j]=you.at(j);
                }
            }
            rot(v,N);
            grav(v,N);
			for(int i=0;i<N;i++)
			{
				for(int j=0;j<N;j++)
					cout<<v[i][j];
				cout<<endl;
			}
            for(int i=0;i<N;i++)
            {
                for(int j=0;j<N;j++)
                {
                    if(v[i][j]=='.')
                        continue;
                    if(checkR==false)
                    {
                     if(v[i][j]=='R')
                    {
                        for(int k=j;k<N;k++)
                        {
                            if(v[i][k]=='R')
                            {
                                cR++;
                            }
                            else
                                break;
                        }
                        if(cR==K)
                            {
                                checkR=true;
                                break;
                            }
                            cR=0;
                        for(int k=i;k<N;k++)
                        {
                            if(v[k][j]=='R')
                            {
                                cR++;
                            }
                            else
                                break;
                        }
                        if(cR==K)
                        {
                            checkR=true;
                            break;
                        }
                        cR=0;
                        int a=j;
                        for(int k=i;k<N;k++)
                        {
                            if(i==0){
                            if(v[k][k]=='R')
                            {
                                cR++;
                            }
                            else
                                break;}

                            else if(i!=0)
                            {
                                if(v[k][a]=='R'&& a<N)
                            {
                                cR++;
                                a++;
                            }
                            else
                                break;
                            }
                        }
                        if(cR==K)
                        {
                            checkR=true;
                            break;
                        }
                        cR=0;
                        int b=j;
                        for(int k=i;k<N;k++)
                        {
                            if(i==0){
                            if(v[k][k]=='R')
                            {
                                cR++;
                            }
                            else
                                break;}

                            else if(i!=0)
                            {
                                if(v[k][b]=='R' && b>=0)
                            {
                                cR++;
                                b--;
                            }
                            else
                                break;
                            }
                        }
                        if(cR==K)
                        {
                            checkR=true;
                            break;
                        }

                        }

                    }
                    if(checkB == false) {
                    if(v[i][j]=='B')
                    {
                        for(int k=j;k<N;k++)
                        {
                            if(v[i][k]=='B')
                            {
                                cB++;
                            }
                            else
                                break;
                        }
                        if(cB==K)
                            {
                                checkB=true;
                                break;
                            }
                            cB=0;
                        for(int k=i;k<N;k++)
                        {
                            if(v[k][j]=='B')
                            {
                                cB++;
                            }
                            else
                                break;
                        }
                        if(cB==K)
                        {
                            checkB=true;
                            break;
                        }
                        cB=0;
                        int a=j;
                        for(int k=i;k<N;k++)
                        {
                            if(i==0){
                            if(v[k][k]=='B')
                            {
                                cB++;
                            }
                            else
                                break;}

                            else if(i!=0)
                            {

                                if(v[k][a]=='B'&& a<N)
                            {
                                cB++;
                                a++;
                            }
                            else
                                break;
                            }
                        }
                        if(cB==K)
                        {
                            checkB=true;
                            break;
                        }
                        cB=0;
                        int b=j;
                        for(int k=i;k<N;k++)
                        {
                            if(i==0){
                            if(v[k][k]=='B')
                            {
                                cB++;
                            }
                            else
                                break;}

                            else if(i!=0)
                            {
                                if(v[k][b]=='B' && b>=0)
                            {
                                cB++;
                                b--;
                            }
                            else
                                break;
                            }
                        }
                        if(cB==K)
                        {
                            checkB=true;
                            break;
                        }

                    }}
                }
            }

            if(checkR && checkB)
            outfile<<"Case #"<<cou+1<<": "<<"Both"<<endl;
            else if(checkR && !checkB)
                outfile<<"Case #"<<cou+1<<": "<<"Red"<<endl;
            else if(checkB && !checkR)
                outfile<<"Case #"<<cou+1<<": "<<"Blue"<<endl;
             else
                outfile<<"Case #"<<cou+1<<": "<<"Neither"<<endl;
            cou++;
            checkB=false;checkR = false;
            delete []v;
        }
		system("pause");
        return 0;
    }
    void grav(char **x,int siz)
    {
        int y=0;
        while(y<siz) {
        char temp;
        for(int i=0;i<siz;i++)
        {
            for(int j=0;j<siz;j++)
            {
                if(x[i][j]=='.')
                    continue;
                else
                {
                    if(i+1<siz){
                    if(x[i+1][j]=='.')
                    {
                        temp = x[i][j];
                        x[i][j]=x[i+1][j];
                        x[i+1][j]=temp;
                    }}
                }
            }
        }y++;
        }
    }
    void rot(char **x,int siz)
    {
        char **temp = new char *[siz];
        for(int i=0;i<siz;i++)
        {
            temp[i]=new char[siz];
        }
         for(int i=0;i<siz;i++)
        {
            for(int j=0;j<siz;j++)
            {
                temp[i][j]=x[i][j];
            }
        }
        for(int i=0;i<siz;i++)
        {
            for(int j=0;j<siz;j++)
            {
                temp[j][i]=x[siz-1-i][j];
            }
        }
        for(int i=0;i<siz;i++)
        {
            for(int j=0;j<siz;j++)
            {
                x[i][j]=temp[i][j];
            }
        }

    }



	*/


    /*string x="zejp mysljylc kd kxveddknmc re jsicpdrysi";
        string y="qde kr kd eoya kw aej tysr re ujdr lkgc jv";
        string z="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
        string x1="qour language is impossible to understand";

        string z1="there are twenty six factorial possibilities";

        string y1="zso it is okay if you want to just give up";
        int *xg=new int [x.size()];
            int *yg=new int[y.size()];
            int *zg=new int[z.size()];
            for(int i=0;i<x.size();i++)
            {
                xg[i]=x[i]-x1[i];
            }
            for(int j=0;j<z.size();j++)
            {
                zg[j]=z[j]-z1[j];
            }
            for(int k=0;k<y.size();k++)
            {
                yg[k]=y[k]-y1[k];
            }
        string input;
        char abdo[3];
        int testcases;
        ifstream infile("A-small-practice.in");
        ofstream outfile("answer.txt");
        getline(infile,input);
        for(int s=0;s<input.size();s++)
        {
            abdo[s]=input.at(s);
        }
        string::size_type sz=0;
        testcases = atoi(abdo);
        int cou=0;
        string output;
        while(cou<testcases)
        {
            getline(infile,input);
            output=input;
            for(int i=0;i<input.size();i++)
            {
               for(int j=0;j<x.size();j++)
               {
                if(output.at(i)==x.at(j))
                {
                    output.at(i)=output.at(i)-xg[j];
                    break;
                }
                else if(output.at(i)==y.at(j))
                {
                    output.at(i)-=yg[j];
                    break;
                }
                else if(output.at(i)==z.at(j))
                {
                    output.at(i)-=zg[j];
                    break;
                }
               }

            } outfile<<"Case #"<<cou+1<<": "<<output<<endl;
                cou++;
        }*/


/*#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <stdlib.h>
#include <fstream>
#include <math.h>
#include<cmath>
#include <iomanip>
#include <stdint.h>
#include "bigint.h"
using namespace std;

int main()
{	
	
	ubigint<81920*6> re;
//	cout<<sizeof(i);
	ifstream infile("C-large-practice.in");
	ofstream outfile("C-large-practice.txt");
	string temp;
	string::size_type sz=0;
	int testcases;
	getline(infile,temp);
	testcases=stoi(temp,&sz,10);
	long double in=3+sqrt(5.0);
	int cou=0;
	long double n;
	
	unsigned long long result;
	int x=0;char c[4];c[3]='\0';
	while(cou<testcases)
	{	
		getline(infile,temp);
		sz=0;
		n=stoll(temp,&sz,10);
		re =pow(in,n);
		for(int i=2;i>=0;i--)
		{	
			c[i]=(re%10)+48;
			re=re/10;
		}
		x=atoi(c);
		outfile<<"Case #"<<cou+1<<": "<<c<<endl;
		cou++;
	}
	
	system("pause");
	return 0;
}*/