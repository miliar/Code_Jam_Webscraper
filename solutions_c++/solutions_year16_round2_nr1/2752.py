#include <bits/stdc++.h>
using namespace std;

int main() {
	 freopen("ILLAST.txt","r",stdin);
	    freopen("LARLAST.txt","w",stdout);
	int t,i;
	string s;
	int num[2000];
	map<char , int > M[26];
		scanf("%d",&t);
for(int j=0;j<t;j++)
	{int A[26]={0};
	    cin>>s;
	int p=0;
	for(i=0;i<s.length();i++)
    {
        A[s[i]-65]++;
    }
    i=s.length();
    while(i>0)
    {
        if(A[25]>0)
        {
            A[4]=A[4]-A[25];
            A[82-65]=A[82-65]-A[25];
            A[79-65]-=A[25];
            while(A[25]--)
            {
                num[p++]=0;
               i=i-4;
            }

        }
        if(A[22]>0)
        {
            //A[4]=A[4]-A[22];
            A[84-65]=A[84-65]-A[22];
            A[79-65]-=A[22];
            while(A[22]--)
            {
                num[p++]=2;
               i=i-3;
            }
        }
         if(A[23]>0)
        {
            //A[4]=A[4]-A[22];
            A[83-65]=A[83-65]-A[23];
            A[73-65]-=A[23];
            while(A[23]--)
            {
                num[p++]=6;
                 i=i-3;
            }
        }
         if(A[18]>0)
        {
            //A[4]=A[4]-A[22];
            A[69-65]=A[69-65]-2*A[18];
            A[86-65]-=A[18];
            A[78-65]-=A[18];
            while(A[18]--)
            {
                num[p++]=7;
                 i=i-5;
            }
        }
        if(A[21]>0)
        {
            //A[4]=A[4]-A[22];
            A[69-65]=A[69-65]-A[21];
            A[70-65]-=A[21];
            A[73-65]-=A[21];
            while(A[21]--)
            {
                num[p++]=5;
                i=i-4;
            }
        }
        if(A[5]>0)
        {
            //A[4]=A[4]-A[22];
            A[79-65]=A[79-65]-A[5];
            A[85-65]-=A[5];
            A[82-65]-=A[5];
            while(A[5]--)
            {
                num[p++]=4;
              i=i-4;
            }
        }
        if(A[14]>0)
        {
            //A[4]=A[4]-A[22];
            A[78-65]=A[78-65]-A[14];
            A[69-65]-=A[14];
           // A[82-65]-=A[14];
            while(A[14]--)
            {
                num[p++]=1;
                i=i-3;
            }
        }

        if(A[6]>0)
        {
            //A[4]=A[4]-A[22];
            A[73-65]=A[73-65]-A[6];
            A[69-65]-=A[6];
            A[84-65]-=A[6];
            A[72-65]-=A[6];
            while(A[6]--)
            {
                num[p++]=8;
                 i=i-5;
            }

        }
        if(A[8]>0)
        {
            //A[4]=A[4]-A[22];
            A[69-65]=A[73-65]-A[8];
            A[78-65]-=2*A[8];
            //A[84-65]-=A[6];
            //A[72-65]-=A[6];
            while(A[8]--)
            {
                num[p++]=9;
                i=i-4;
            }
        }
        while(A[84-65]--)
            {
                num[p++]=3;
                i=i-5;
            }

    }
    std::sort(num,num+p);

    cout<<"Case #"<<j+1<<": ";
    for(int l=0;l<p;l++)
    {

        cout<<num[l];
    }
cout<<endl;
      	//printf("Case #%d: %s\n",j+1,s1);


	}

	// your code goes here
	return 0;
}
