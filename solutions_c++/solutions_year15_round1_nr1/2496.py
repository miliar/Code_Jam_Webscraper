// 1st.cpp : Defines the entry point for the console application.
//

#include "StdAfx.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <stdlib.h>
using namespace std;
int ncase;
void main()
{
		freopen("file.in", "r", stdin);
		freopen("file.out", "w", stdout);
		scanf("%d",&ncase);
		int m1,m2,n,rate;
		int m[1000];
		for(int i=1;i<=ncase;i++){
			m1=0;
			m2=0;
			rate=0;
			scanf("%d",&n);
			for(int j=0;j<n;j++){
				scanf("%d",&m[j]);
			}
			for(int j=0;j<n-1;j++){
				if(m[j+1]<m[j]){
					m1+=m[j]-m[j+1];
					if(rate< (m[j]-m[j+1]))
						rate=m[j]-m[j+1];
				}	
			}

			for(int j=0;j<n-1;j++){
				if(m[j]<rate)
					m2+=m[j];
				else if(m[j]>=rate)
					m2+=rate;
			}

			cout<<"Case #"<<i<<": "<<m1<<" "<<m2<<endl;
		}
		//system("PAUSE");
}

