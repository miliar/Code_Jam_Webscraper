#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <inttypes.h>
using namespace std;
int main()
{
  long T,N,M;
  long o[1005];
  long e[1005];
  long p[1005];
  long numberofpeople[1005];
  long points[2010];
  long temp,i,j,k,l;
  long actual,cost,lastindex,last,diff,number,temp1,temp2,first,tempmod;
  cin >> T;
  for(i=0;i<T;i++){
	cin >> N;
	cin >> M;
	cost =0;
	actual =0;
	for(j=0;j<1005;j++){
		o[j]=0;
		e[j]=0;
		p[j]=0;
		numberofpeople[j]=0;
	}
	for(j=0;j<2010;j++){
		points[j]=0;
	}
	for(j=0;j<M;j++){
		cin >> temp;
		o[j]= temp;
		points[2*j]=temp;	
		cin >> temp;
		e[j]=temp;
		points[2*j+1]= temp;
		cin >> temp;
		p[j]=temp;		
		diff = e[j] - o[j];
		tempmod = (diff*(2*N - diff +1)/2)%1000002013;
		tempmod = (tempmod*p[j])%1000002013;
		actual = (actual + tempmod)%1000002013;
	}
	sort(points,points+2*M);
//	for(j=0;j<2*M;j++){
//		cout << points[j] << " ";
//	}
//	cout << endl;
	for(j=0;j<2*M;j++){
		if(j ==0 || (j >0 && points[j] >points[j-1])){
			for(k=0;k<M;k++){
				if(points[j] == o[k]){
					numberofpeople[k]=numberofpeople[k]+p[k];
				}
			}
			for(k=0;k<M;k++){
				if(points[j] == e[k]){
					last= 0;
					lastindex =0;
					number = p[k];
	//				cout << k <<" " << number << " " << e[k] << endl;
	//				cout<< numberofpeople[0] << " " << numberofpeople[1] << endl;
					while(number>0){						
						last= 0;
						lastindex =0;
						for(l=0;l<M;l++){
							if(o[l]>= last && numberofpeople[l] > 0){
								last = o[l];
								lastindex = l;
							}
						}
			//			cout << lastindex << endl;
	//					cout << lastindex << " " << numberofpeople[lastindex] <<endl;
						temp1 = number;
						temp2 = numberofpeople[lastindex];
						number = max(temp1-temp2,long(0));
						numberofpeople[lastindex] = max(temp2-temp1,long(0));
						diff = e[k] - o[lastindex];
//						cout << "diff " << diff << endl;
						if(temp1 >=temp2){							
							tempmod = (diff*(2*N - diff +1)/2)%1000002013;
							tempmod = (temp2*tempmod)%1000002013;
							cost = (cost +tempmod)%1000002013;
						}else{					
							tempmod = (diff*(2*N - diff +1)/2)%1000002013;
							tempmod = (temp1*tempmod)%1000002013;
							cost = (cost +tempmod)%1000002013;
						}
					}
				}
			}
		}	
				
	}
	
	tempmod = actual - cost;
	tempmod = (tempmod)%1000002013;
	tempmod = tempmod + 1000002013;
	cout << "Case #" << i+1 << ": " << ((tempmod)%1000002013) << endl;
	
		
  }
  return 0;
}
