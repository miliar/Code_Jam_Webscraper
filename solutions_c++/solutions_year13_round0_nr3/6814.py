#include<iostream>
#include<stdio.h>
#include<map>
#include<string>
#include<vector>
#include<math.h>
using namespace std;
/*vector<string> splitEx(const string& src, string separate_char)   
{   
    vector<string> strs;   
       
    int separate_Len = separate_char.size();  
    int lastPosition = 0,index = -1;   
    while (-1 != (index = src.find(separate_char,lastPosition)))   
    {   
        strs.push_back(src.substr(lastPosition,index - lastPosition));   
        lastPosition = index + separate_Len;   
    }   
    string lastString = src.substr(lastPosition);   
    if (!lastString.empty())   
        strs.push_back(lastString);
    return strs;   
}   
  */
/*
int get1toN(int n)
{
	return (n)*(n-1)/2;
}
int getResult(int M, int N, int k)//M<N
{

	int ret = 0;
   int row,col;
	int q = sqrt(k);
	if(q<M)
	{
		if(q*(q+1)<k)
		{
			col=q+1;
		}
		else
		{
			col =q;
		}
		row =k/col;
	}
	if(q>=M)
	{
		col =M;
		row = k/col;
	}
		ret = ret+get1toN(row)*get1toN(col);
		ret = ret+(row)*get1toN(k%(row*col));

	
	return ret;
}*/
int decompose(int in, int arr[], int &len)
{
	len=0;
	
	while(in)
	{
		arr[len++]=in%10;
		in=in/10;
	}
	return 0;
}
enum{
	yes=1,
	no=0,
};
int checkP(int in)
{
	int ret=yes;
	int len=0;
	int arr[15];
	decompose(in, arr,len);
	for(int i=0;i<=(len-1)/2;i++)
	{
		if(arr[i]!=arr[len-i-1])
		{
			ret=no;
			break;
		}
	}
	return ret;

}
int checkS(int in)
{
	int s=sqrt(in);
	if(s*s==in)
	{
		return yes;
	}
	else{
		return no;
	}
}
#define MAX 1000
int getNumbers(int arr[],int min, int max)
{
	int i=0;
	int minI =0;
	while(true)
	{
		if(min<=arr[i])
		{
			minI=i;
			break;
		}
		i++;
	}
	int maxI = 0;
	int j=i;
	while(true)
	{
		if(max<=arr[j])
		{
			maxI=j;
			break;
		}
		j++;
	}
	int ret =maxI-minI;
	if(arr[maxI]==max)
	{ 
		ret =ret+1;
	}
	return ret;
}
int main(void)
{
	int T;
	cin>>T;
	int dataA[1000];
	int dataB[1000];
	int i=0;
	int LT =T;
	while(LT--)
	{
		cin>>dataA[i];
		cin>>dataB[i];
		i++;
	}
	int max=MAX;
	int FandS[MAX];
	int j=0;
	for(int i=1;i<max;i++)
	{
		if(checkP(i)&&checkP(i*i))
		{
			FandS[j]=i*i;
			j++;
		}

	}
	int time = 1;
	while(T--)
	{
		cout<<"Case #"<<time<<": "<<getNumbers(FandS,dataA[time-1],dataB[time-1])<<endl;
		time++;
	}
	/*int a;
	cin>>a;
	int time=0;
	while(a--)
	{
		time++;
		int M;int N; int k;
		cin>>M;
		cin>>N;
		cin>>k;
		if(M>N)
		{
			int temp = M;
			int M=N;
			int N=temp;
		}
		cout<<"Case #"<<time<<": "<<getResult(M,N,k)<<endl;
	}
	*/
    				return 0;
}

    	/*
    	int T;
		scanf("%d",&T);
    	
		std::map<string,string> dic;// = new map<string,string>();
    	int N;
		int M;
		int time =0;
    	while(T--) {
			dic.clear();
    		time++;
    		cin>> N;// scanf("%d",&N);
    		cin>> M; //scanf("%d",&M);
    		while(M--)
    		{
				string key;
				string value;
				cin>>key;//scanf("%s",&key);
				cin>>value;//scanf("%s",&value);
				dic[key]= value;
    		}
		string s;
		getline(cin,s);
		getline(cin,s);
		vector<string> ss = splitEx(s," ");
		//if(N%2==0)
    	//{
		while(--N){
					int sL = ss.size();
    				while(sL--)
    				{
						string key = ss[sL];
					   map<string,string>::iterator itt=dic.find(key);
    					if(itt!=dic.end())
    					{
    					//	String key = ss[sL];
    					    ss[sL] = dic[key];
    					}
						else
						{
						}
    				}
		}

		cout<<"Case #";
		cout<<time<<": ";
		for(int i = 0;i< ss.size();i++)
		{
			cout<<ss[i];
			if(i!=ss.size())
			{
				cout<<" ";
			}
			
		}
		cout<<endl;
		}
		*/
