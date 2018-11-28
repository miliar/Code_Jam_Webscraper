#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string.h>
using namespace std;
int N,L;
string words[100];
int minMove(string a,string b){
    int len1=a.size();
    int len2=b.size();
    int posa=0,posb=0;
    int min=0;
    int numa=0,numb=0;
    while(posa<len1||posb<len2){
        char apos=a[posa];
        char bpos=b[posb];
        if(apos!=bpos)
            return -1;

        while(a[posa]==apos){
            numa++;
            posa++;
        }
        while(b[posb]==bpos){
            numb++;
            posb++;
        }
        int diff=(numa-numb);
        if(diff<0)
            diff=numb-numa;
        min+=diff;
        numa=0;
        numb=0;
    }
    return min;
}
int main()
{
	int	x;
	int A,B,K,sum;

	 int test_cases;
   freopen("g:/input.txt","r",stdin);
    freopen("g:/output.txt","w",stdout);

    cin>>test_cases;
    for(int caseNum=0;caseNum<test_cases;caseNum++)
    	{
		cin>>A;
		cin>>B;
		cin>>K;
		sum = 0;
			for(int i=0 ;i<A; i++)
				for(int j=0 ;j<B; j++)
				{
					x = i & j;
					if(x<K)
						sum++;
				}

		cout<<"Case #"<<caseNum+1<<": "<<sum<<endl;

	}
	return 0;
}

/*{
    int test_cases;
    freopen("g:/input.txt","r",stdin);
    freopen("g:/output.txt","w",stdout);

    cin>>test_cases;
    int marks[200];
    double sum=0;
    double avg=0;
    bool status[200];
    string str1,str2;

  //  char grids[6][6];
    for(int caseNum=0;caseNum<test_cases;caseNum++){
        cin>>N;
        cin>>str1;
        cin>>str2;
        int move=minMove(str1,str2);



        cout<<"Case #"<<caseNum+1<<": ";
        if(move>-1)
        cout<<move;
        else
        cout<<"Fegla Won";

        cout<<endl;

    }
    return 0;
    }

*/
