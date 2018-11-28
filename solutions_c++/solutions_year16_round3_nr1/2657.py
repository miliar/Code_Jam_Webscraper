// Google1.cpp: определяет точку входа для консольного приложения.
//
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <string.h> 
#include "StdAfx.h"
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
_int64 MyPow(int a,int b){
	_int64 s=1;
	for (int i=1;i<=b;i++){
		s=s*a;
	}
	return s;
}
void main() {
	//ios::sync_with_stdio(false);
	FILE *fin = freopen("A-large.in", "r", stdin);
	//assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
  // read t. cin knows that t is an int, so it reads it as such.
  
	_int64 t;
	cin>>t;
	
	for (_int64 k=1; k<=t; k++){
		string alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		int *p=new int[30];
		int n;
		int s=0;
		cin>>n;
		int max1=0;
		int i1=0;
		int max2=0;
		int i2;
		for(int i=0;i<n;i++){
			cin>>p[i];
			s=s+p[i];
			
		}
		string exit="";
		while(s>0){
			max1=0;
			max2=0;
			/*for (int i=0;i<n;i++)
				cout<<p[i]<<" ";
			cout<<endl;*/
			for(int i=0;i<n;i++){
			
				
				if (max1<p[i]) {
					max1=p[i];
					i1=i;
				}
				
			}
			if (s>0){
				p[i1]=p[i1]-1;
				s--;
				exit=exit+" "+alp[i1];
			}
			/*for (int i=0;i<n;i++)
				cout<<p[i]<<" ";
			cout<<endl;*/
			max2=0;
			int kol=1;
			if (s>0){
				for(int i=0;i<n;i++){
			
					
					if (max2<p[i]) {
						max2=p[i];
						i2=i;
						kol=1;
					}
					else if (max2==p[i]){
						kol=kol+1;
						/*cout<<"i="<<i<<endl;*/
					}
				}
				/*cout<<kol<<endl;*/
				
				if ((kol==1)){
					p[i2]--;
					s--;
					exit=exit+alp[i2];
				}
			}
			/*for (int i=0;i<n;i++)
				cout<<p[i]<<" ";
			cout<<endl;*/
			//cout<<s<<endl;
			exit=exit;
		}

		cout<<"Case #"<<k<<":"<<exit<<endl;
	}
}


//void mainB() {
//	//ios::sync_with_stdio(false);
//	//FILE *fin = freopen("A-small-attempt3.in", "r", stdin);
//	//assert( fin!=NULL );
//	//FILE *fout = freopen("A-small-attempt3.out", "w", stdout);
//  // read t. cin knows that t is an int, so it reads it as such.
//  
//	_int64 t;
//	cin>>t;
//	
//	for (_int64 k=1; k<=t; k++){
//		string c,j;
//		cin>>c>>j;
//		//cout<<c;
//		int *a=new int[20];
//		int *b=new int[20];
//		_int64 sa=0;
//		_int64 sb=0;
//		int *ai=new int [20];
//		int *bi=new int[20];
//		int kb=0;
//		for (int i=0;i<c.length();i++){
//			a[i]=c[i]-'0';
//			b[i]=j[i]-'0';
//			if (a[i]>9) {
//				a[i]=0;
//				ai[i]=0;
//			}
//			else ai[i]=1;
//			if (b[i]>9) {
//				b[i]=0;
//				bi[i]=0;
//			}
//			else bi[i]=1;
//			if ((ai[i]==0)&&(bi[i]==1)){
//				a[i]=b[i];
//				
//			}
//			if ((ai[i]==1)&&(bi[i]==0)){
//				b[i]=a[i];
//			}
//			//cout<<a[i]<<" ";
//			sa+=a[i]*MyPow(10,c.length()-i);
//		}
//		_int64 mind=abs(sa-sb);
//		int flag=0;
//		if (mind==0){
//			flag=1;
//		}
//		else for (int i=0;i<2*c.length();i++){
//
//		}
//	}
//
//}

//void mainA() {
//	//ios::sync_with_stdio(false);
//	FILE *fin = freopen("A-small-attempt6.in", "r", stdin);
//	//assert( fin!=NULL );
//	FILE *fout = freopen("A-small-attempt6.out", "w", stdout);
//  // read t. cin knows that t is an int, so it reads it as such.
//  
//	_int64 t;
//	cin>>t;
//	
//	for (_int64 k=1; k<=t; k++){
//		string s;
//		cin>>s;
//		string *ch=new string[10];
//		ch[0]="ZERO";
//		ch[1]="ONE";
//		ch[2]="TWO";
//		ch[3]="THREE";
//		ch[4]="FOUR";
//		ch[5]="FIVE";
//		ch[6]="SIX";
//		ch[7]="SEVEN";
//		ch[8]="EIGHT";
//		ch[9]="NINE";
//		int *a=new int[10];
//		int l=s.length();
//		for (int i=0;i<10;i++){
//			a[i]=0;
//			string s1=s;
//			int chl=ch[i].length();
//			int *let=new int[chl];
//			for (int il=0;il<chl;il++){
//				let[il]=0;
//			}
//			for (int j=0;j<l;j++){
//				for (int j1=0;j1<chl;j1++){
//					if (s1[j]==ch[i][j1]){
//						let[j1]++;
//						s1[j]='.';
//					}
//				}
//
//			}
//			//cout<<i<<" "<<s1<<endl;
//			int min=20000;
//			if (i==3){
//				//cout<<ch[3][3];
//				let[3]=let[3]/2;
//				let[4]=let[4]/2;
//			}
//			if (i==7){
//				let[1]=let[1]/2;
//				let[3]=let[3]/2;
//			}
//			if (i==9){
//				let[0]=let[0]/2;
//				let[2]=let[2]/2;
//			}
//			for (int j1=0;j1<chl;j1++){
//				if (min>let[j1]){
//					min=let[j1];
//				}
//			}
//			//cout<<i<<' '<<min<<endl;
//			a[i]=min;
//			
//
//			s1=s;
//			for (int j1=0;j1<chl;j1++){
//				int m=min;
//				for (int j=0;((j<l)&&(m>0));j++){
//					if (s[j]==ch[i][j1]){
//						s[j]='.';
//						m--;
//					}
//				}
//			}
//		}
//		
//		cout<<"Case #"<<k<<": ";
//		for (int i=0;i<10;i++){
//			for (int ai=1;ai<=a[i];ai++){
//				cout<<i;
//			}
//		}
//	cout<<endl;
//	}
//	
//	//cin>>t;
//}