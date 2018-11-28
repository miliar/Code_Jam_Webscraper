/*
ID: abunida1
PROG: ride
LANG: C++
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
#include <stack>
#include <bitset>
#include <list>
#include <limits.h>

using namespace std;


#define ii pair<int,int>
#define iii pair<int,ii>
#define INF 1000000000
typedef long long int ll;
typedef unsigned long long int ull;
typedef vector <int> vi;
typedef vector <ii> vii;

char peta[60][60];
int t,r,c,m;

void bersih_bersih () {
	for(int i=1;i<=r ;i++){
			for(int j=1;j<=c ;j++){
				if(peta[i][j]=='1' || peta[i][j]=='0'){
					peta[i][j]='.';
				}					
			}
		}
}

bool cek(bool bersih);
bool aman();



void cetak(){
	for(int i=1;i<=r  ;i++){
			for(int j=1;j<=c ;j++){
				printf("%c",peta[i][j]);	
			}
			printf("\n");
		}
		printf("\n");
}

void isi_kosongV5 (int banyak) {
	for(int i=0;i<60;i++)for(int j=0;j<60;j++)peta[i][j]='.';		
	for(int i=1;i<=r;i++)for(int j=1;j<=c;j++)peta[i][j]='*';
	
	queue <ii> s;
	
	s.push( ii(r,c) );
	peta[r][c]='.';
	banyak--;
	
	ii top;
	int i,j;
	
	while(!s.empty()){
		top=s.front();
		s.pop();
		
		i=top.first;
		j=top.second;
		
		
		if(banyak==0)break;
		
		if( j-1 >=1 && peta[i][j-1]=='*'){s.push( ii(i,j-1) );peta[i][j-1]='.';banyak--;if(banyak==0)break;}
		if(i-1>=1 && peta[i-1][j]=='*'){s.push( ii(i-1,j) );peta[i-1][j]='.';banyak--;if(banyak==0)break;}
		//if(i-1>=1 && j-1 >=1 && peta[i-1][j-1]=='*'){s.push( ii(i-1,j-1) );peta[i-1][j-1]='.';banyak--;if(banyak==0)break;}
		//if(i-1>=1 && j+1 <=c && peta[i-1][j+1]=='*'){s.push( ii(i-1,j+1 ) );peta[i-1][j+1]='.';banyak--;if(banyak==0)break;}
		// if(i+1<=r && j-1 >=1 && peta[i+1][j-1]=='*'){s.push( ii(i+1,j-1) );peta[i+1][j-1]='.';banyak--;if(banyak==0)break;}
				
		
		// if( j+1 <=c && peta[i][j+1]=='*'){s.push( ii(i,j+1) );peta[i][j+1]='.';banyak--;if(banyak==0)break;}		
		// if(i+1<=r && peta[i+1][j]=='*'){s.push( ii(i+1,j) );peta[i+1][j]='.';banyak--;if(banyak==0)break;}
		// if(i+1<=r && j+1 <=c && peta[i+1][j+1]=='*'){s.push( ii(i+1,j+1) );peta[i+1][j+1]='.';banyak--;if(banyak==0)break;}
		
	}
	
	while(!s.empty())s.pop();
}

void isi_kosongV4 (int banyak) {
	for(int i=0;i<60;i++)for(int j=0;j<60;j++)peta[i][j]='.';		
	for(int i=1;i<=r;i++)for(int j=1;j<=c;j++)peta[i][j]='*';
	
	int temp=banyak;
	
	for(int i=r;i>=1 && banyak > 0;i--){
		for(int j=c;j>=1 && banyak>0;j--){
			peta[i][j]='.';
			banyak--;
		}
	}
	
	banyak=temp;
	
	if(cek(true)==false){
		for(int i=0;i<60;i++)for(int j=0;j<60;j++)peta[i][j]='.';		
		for(int i=1;i<=r;i++)for(int j=1;j<=c;j++)peta[i][j]='*';
		
		for(int i=c;i>=1 && banyak > 0;i--){
			for(int j=r;j>=1 && banyak>0;j--){
				peta[j][i]='.';
				banyak--;
			}
		}
	}
	
}

void isi_kosongV3 (int banyak) {
	for(int i=0;i<60;i++)for(int j=0;j<60;j++)peta[i][j]='.';		
	for(int i=1;i<=r;i++)for(int j=1;j<=c;j++)peta[i][j]='*';
	
	queue <ii> s;
	
	s.push( ii(r,c) );
	peta[r][c]='.';
	banyak--;
	
	ii top;
	int i,j;
	
	while(!s.empty()){
		top=s.front();
		s.pop();
		
		i=top.first;
		j=top.second;
		
		
		if(banyak==0)break;
		
		if( j-1 >=1 && peta[i][j-1]=='*'){s.push( ii(i,j-1) );peta[i][j-1]='.';banyak--;if(banyak==0)break;}
		if(i-1>=1 && peta[i-1][j]=='*'){s.push( ii(i-1,j) );peta[i-1][j]='.';banyak--;if(banyak==0)break;}
		if(i-1>=1 && j-1 >=1 && peta[i-1][j-1]=='*'){s.push( ii(i-1,j-1) );peta[i-1][j-1]='.';banyak--;if(banyak==0)break;}
		//if(i-1>=1 && j+1 <=c && peta[i-1][j+1]=='*'){s.push( ii(i-1,j+1 ) );peta[i-1][j+1]='.';banyak--;if(banyak==0)break;}
		// if(i+1<=r && j-1 >=1 && peta[i+1][j-1]=='*'){s.push( ii(i+1,j-1) );peta[i+1][j-1]='.';banyak--;if(banyak==0)break;}
				
		
		// if( j+1 <=c && peta[i][j+1]=='*'){s.push( ii(i,j+1) );peta[i][j+1]='.';banyak--;if(banyak==0)break;}		
		// if(i+1<=r && peta[i+1][j]=='*'){s.push( ii(i+1,j) );peta[i+1][j]='.';banyak--;if(banyak==0)break;}
		// if(i+1<=r && j+1 <=c && peta[i+1][j+1]=='*'){s.push( ii(i+1,j+1) );peta[i+1][j+1]='.';banyak--;if(banyak==0)break;}
		
	}
	
	while(!s.empty())s.pop();
}

void isi_kosongV2 (int banyak) {
	for(int i=0;i<60;i++)for(int j=0;j<60;j++)peta[i][j]='.';		
	for(int i=1;i<=r;i++)for(int j=1;j<=c;j++)peta[i][j]='*';
	
	queue <ii> s;
	
	s.push( ii(r,c) );
	peta[r][c]='.';
	banyak--;
	
	ii top;
	int i,j;
	
	while(!s.empty()){
		top=s.front();
		s.pop();
		
		i=top.first;
		j=top.second;
		
		
		if(banyak==0)break;
		
		if(i-1>=1 && j+1 <=c && peta[i-1][j+1]=='*'){s.push( ii(i-1,j+1 ) );peta[i-1][j+1]='.';banyak--;if(banyak==0)break;}
		if(i-1>=1 && peta[i-1][j]=='*'){s.push( ii(i-1,j) );peta[i-1][j]='.';banyak--;if(banyak==0)break;}	
		if(i-1>=1 && j-1 >=1 && peta[i-1][j-1]=='*'){s.push( ii(i-1,j-1) );peta[i-1][j-1]='.';banyak--;if(banyak==0)break;}
		if( j-1 >=1 && peta[i][j-1]=='*'){s.push( ii(i,j-1) );peta[i][j-1]='.';banyak--;if(banyak==0)break;}
		if(i+1<=r && j-1 >=1 && peta[i+1][j-1]=='*'){s.push( ii(i+1,j-1) );peta[i+1][j-1]='.';banyak--;if(banyak==0)break;}
				
		
		// if( j+1 <=c && peta[i][j+1]=='*'){s.push( ii(i,j+1) );peta[i][j+1]='.';banyak--;if(banyak==0)break;}		
		// if(i+1<=r && peta[i+1][j]=='*'){s.push( ii(i+1,j) );peta[i+1][j]='.';banyak--;if(banyak==0)break;}
		// if(i+1<=r && j+1 <=c && peta[i+1][j+1]=='*'){s.push( ii(i+1,j+1) );peta[i+1][j+1]='.';banyak--;if(banyak==0)break;}
		
	}
	
	while(!s.empty())s.pop();
}

void isi_kosongV1(int banyak){

	for(int i=0;i<60;i++)for(int j=0;j<60;j++)peta[i][j]='.';		
	for(int i=1;i<=r;i++)for(int j=1;j<=c;j++)peta[i][j]='*';
	
	queue <ii> s;
	
	s.push( ii(r,c) );
	peta[r][c]='.';
	banyak--;
	
	ii top;
	int i,j;
	
	while(!s.empty()){
		top=s.front();
		s.pop();
		
		i=top.first;
		j=top.second;
		
		
		if(banyak==0)break;
		
		if(i+1<=r && j-1 >=1 && peta[i+1][j-1]=='*'){s.push( ii(i+1,j-1) );peta[i+1][j-1]='.';banyak--;if(banyak==0)break;}
		if( j-1 >=1 && peta[i][j-1]=='*'){s.push( ii(i,j-1) );peta[i][j-1]='.';banyak--;if(banyak==0)break;}		
		if(i-1>=1 && j-1 >=1 && peta[i-1][j-1]=='*'){s.push( ii(i-1,j-1) );peta[i-1][j-1]='.';banyak--;if(banyak==0)break;}		
		if(i-1>=1 && peta[i-1][j]=='*'){s.push( ii(i-1,j) );peta[i-1][j]='.';banyak--;if(banyak==0)break;}		
		if(i-1>=1 && j+1 <=c && peta[i-1][j+1]=='*'){s.push( ii(i-1,j+1 ) );peta[i-1][j+1]='.';banyak--;if(banyak==0)break;}
		
		
		// if( j+1 <=c && peta[i][j+1]=='*'){s.push( ii(i,j+1) );peta[i][j+1]='.';banyak--;if(banyak==0)break;}		
		// if(i+1<=r && peta[i+1][j]=='*'){s.push( ii(i+1,j) );peta[i+1][j]='.';banyak--;if(banyak==0)break;}
		// if(i+1<=r && j+1 <=c && peta[i+1][j+1]=='*'){s.push( ii(i+1,j+1) );peta[i+1][j+1]='.';banyak--;if(banyak==0)break;}
		
	}
	
	while(!s.empty())s.pop();
	
}

bool aman (int i,int j){
	
	if(peta[i-1][j-1]=='*')return false;
	if(peta[i-1][j]=='*')return false;
	if(peta[i-1][j+1]=='*')return false;
	
	if(peta[i][j-1]=='*')return false;
	if(peta[i][j+1]=='*')return false;
	
	if(peta[i+1][j-1]=='*')return false;
	if(peta[i+1][j]=='*')return false;
	if(peta[i+1][j+1]=='*')return false;
	
	return true;
}

bool cek(bool bersih){
		peta[r][c]='0';
		
		stack <ii> s;
		s.push( ii(r,c) );
		
		ii top;
		int i,j;
		while(!s.empty()){
			top=s.top();
			s.pop();
			i=top.first;
			j=top.second;
			
			
			
			if(aman(i,j)==false){
				peta[i][j]='1';
				continue;
			}//kalo ga aman ga bisa push
			
			if(i-1>=1 && j-1 >=1 && peta[i-1][j-1]=='.'){s.push( ii(i-1,j-1) );peta[i-1][j-1]='0';}
			if(i-1>=1 && peta[i-1][j]=='.'){s.push( ii(i-1,j) );peta[i-1][j]='0';}
			if(i-1>=1 && j+1 <=c && peta[i-1][j+1]=='.'){s.push( ii(i-1,j+1 ) );peta[i-1][j+1]='0';}
			
			if( j-1 >=1 && peta[i][j-1]=='.'){s.push( ii(i,j-1) );peta[i][j-1]='0';}
			if( j+1 <=c && peta[i][j+1]=='.'){s.push( ii(i,j+1) );peta[i][j+1]='0';}
			
			if(i+1<=r && j-1 >=1 && peta[i+1][j-1]=='.'){s.push( ii(i+1,j-1) );peta[i+1][j-1]='0';}
			if(i+1<=r && peta[i+1][j]=='.'){s.push( ii(i+1,j) );peta[i+1][j]='0';}
			if(i+1<=r && j+1 <=c && peta[i+1][j+1]=='.'){s.push( ii(i+1,j+1) );peta[i+1][j+1]='0';}
			
			
		}
		
		//cetak();
		
				
		for(int i=1;i<=r ;i++){
			for(int j=1;j<=c ;j++){
				if(peta[i][j]=='.'){
					if(bersih)bersih_bersih();
					return false;
				}					
			}
		}
		
		if(bersih)bersih_bersih();
		

		
		return true;
}



int main (){

	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	//freopen("friday.in","r",stdin);	freopen("friday.out","w",stdout);
	
	
	
	scanf("%d",&t);
	
	int kasus=1;
	
	while(t--){
		printf("Case #%d:\n",kasus++);
		scanf("%d %d %d",&r,&c,&m);	
		
		
		isi_kosongV1(r*c-m);
		bool betul=false;
		
		if(cek(true)==false){
			isi_kosongV2(r*c-m);
			
			if(cek(true)==true)betul=true;
			else{
				
				isi_kosongV3(r*c-m);				
				
				if(cek(true)==true )betul=true;
				else{
					isi_kosongV4(r*c-m);
					
					if(cek(true))betul=true;
					else{
						isi_kosongV5(r*c-m);
						
						if(cek(true)==true)betul=true;
						else{
						
						}
					}
				}
			}
		}
		else betul=true;
		
		//cek(false);	cetak();
		
		if(betul){
			
			peta[r][c]='c';
				
			for(int i=1;i<=r ;i++){
				for(int j=1;j<=c ;j++){
					if(peta[i][j]=='0' || peta[i][j]=='1')peta[i][j]='.';
					printf("%c",peta[i][j]);	
				}
				printf("\n");
			}
		
		}
		else printf("Impossible\n");
		
		
		
		
	}

	
	return 0;
}
















