#include <iostream>
#include <climits>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <utility>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;


int board[200][200];

string judge(int N, int M)
{
	vector<int> vrow(N,0);
	vector<int> vcol(M,0);
	for(int i=0;i<N;i++)
		vrow[i]=i;
	for(int i=0;i<M;i++)
		vcol[i]=i;
	while(vrow.size()>0&&vcol.size()>0)
	{
		int p=0,q=0,minv=INT_MAX;
		for(int i=0;i<vrow.size();i++)
			for(int j=0;j<vcol.size();j++)
		{
			int r=vrow[i],c=vcol[j];
			if(board[r][c]<minv)
			{
				minv=board[r][c];
				p=r;q=c;
			}
		}
		//judge row or col is same
		bool irowsame=true;
		for(int j=0;j<vcol.size();j++)
		{		
			int c=vcol[j];
			if(board[p][c]!=minv)
			{
				irowsame=false;
				break;
			}
		}
		if(irowsame==true)
		{
			vrow.erase(remove(vrow.begin(),vrow.end(),p),vrow.end());
                        continue;
		}
		bool icolsame=true;
		for(int i=0;i<vrow.size();i++)
		{
			int r=vrow[i];
			if(board[r][q]!=minv)
			{
				icolsame=false;	
				break;
			}
		}
		if(icolsame==true)
		{
			vcol.erase(remove(vcol.begin(),vcol.end(),q),vcol.end());
			continue;
		}
		return "NO";
		
	}
	return "YES";	
	
}

int main() {
 
        int T;
        cin>>T;
        int count=1;
        
        while(T--)
        {
		int N, M;
		cin>>N>>M;
                for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
			{
				int aij;
				cin>>aij;
				board[i][j]=aij;
			}

                cout<<"Case #"<<count++<<": "<<judge(N,M)<<endl;
         }



        return 0;
}
