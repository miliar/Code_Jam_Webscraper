#include<iostream>
using namespace std;


int arr[53][53] = {0};

void print(int r, int c){
	
	for(int i=1; i<=r; i++){
		for(int j=1; j<=c; j++){
			if(arr[i][j] == 0){
				cout<<".";
			}
			if(arr[i][j] == 1){
				cout<<"*";
			}
			if(arr[i][j] == 2){
				cout<<"c";
			}
		}	
		cout<<endl;
	}

}

int main(){

	int t;
	cin>>t;
	int r,c,count;
	int test = 1;
	while(t--){
	cout<<"Case #"<<test<<":"<<endl;
	test++;
	cin>>r>>c>>count;
	//cout<<r<<" "<<c<<endl;
	if(r==1 && c==1){
		cout<<"c"<<endl;
		continue;
	}

	if(r>2 && c>2){
			int left = r*c - count;
			if(left==0 || left == 2 || left == 3 || left == 5 || left == 7){
				cout<<"Impossible"<<endl;
				continue;
			}
	
			for(int i=1; i<=r-2 && count>0 ; i++){
				for(int j=1; j<=c-2 && count>0 ; j++){
					arr[i][j] = 1;
					count--;
					//print(r,c);
				}
			}

			for(int i=1; i<=r-3 && count>0 ; i++){
			
				arr[r-2][c-2] = 0;
				arr[i][c] = 1;
				arr[i][c-1] = 1;
	
				count--;
					//print(r,c);
				if(count>0){
					arr[r-2][c-2] = 1;
					count--;
				}	
					//print(r,c);
				
	
			}
			for(int j=1; j<=c-3 && count>0 ; j++){
				arr[r-2][c-2] = 0;
				arr[r][j] = 1;
				arr[r-1][j] = 1;
				count--;
					//print(r,c);
				if(count>0){
					arr[r-2][c-2] = 1;
					count--;
				}	//print(r,c);
			}
			if(count>0){
				arr[r-2][c-1] = 1;
				arr[r-2][c] = 1;
				count = count -2;
			}
			if(count>0){
				//cout<<"tooooooo"<<endl;
				arr[r-1][c-2] = 1;
				arr[r][c-2] = 1;
				count = count - 2;
			}
			if(count>0){
				arr[r-1][c-1] = 1;
				arr[r-1][c] = 1;
				arr[r][c-1] = 1;
			}
			arr[r][c] = 2;
			print(r,c);

		}
		else{
			int m = min(r,c);
			if(m==1){
				int left = r*c - count;
				if(left==0){
					cout<<"Impossible"<<endl;
				}
				if(r==1){
					for(int i=1; i<=count; i++){
						arr[1][i] = 1;
					}		
					arr[r][c] = 2;
					print(r,c);
		
				}
				else if(c==1){
					for(int i=1; i<=count; i++){
						arr[i][1] = 1;
					}
					arr[r][c] = 2;
					print(r,c);
				}		
	
			}
			if(m==2){
				int left = r*c - count;
				if(left==1){
					for(int i=1;i<=r;i++){
						for(int j=1; j<=c; j++){
							
							if(i==r && j==c){
								cout<<"c";
							}
							else{
								cout<<"*";
							}
						}
						cout<<endl;
						
					}
					continue;
				}
				if(left==0 || left==2 || left%2!=0){
					cout<<"Impossible"<<endl;
					continue;
				}
				if(r==2){
					for(int i=1; i<=count/2; i++){
						arr[1][i] = 1;
						arr[2][i] = 1;
					}
					arr[r][c] = 2;
					print(r,c);
				}
				else if(c==2){
				
					for(int i=1; i<=count/2; i++){
						arr[i][2] = 1;
						arr[i][1] = 1;
					}
					arr[r][c] = 2;
					print(r,c);
				}
			}
		}		

		for(int i=1; i<=r; i++){
			for(int j=1; j<=c; j++){
				arr[i][j] = 0;
			}
		}
	}

}
