#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream in("input.txt");
    ofstream out("output.txt");
	
	int T;
	in>>T;
	for(int i = 0 ; i < T ; i++){
		int ans1 = 0;
		int ans2 = 0;
		int a1 = 0, a2 = 0;
		int arr1[4][4] = {0,};
		int arr2[4][4] = {0,};
		
		in>>a1;
		for(int j = 0 ; j < 4 ; j++)
			for(int k = 0 ; k < 4 ; k++)
				in>>arr1[j][k];
		
		in>>a2;
		for(int j = 0 ; j < 4 ; j++)
			for(int k = 0 ; k < 4 ; k++)
				in>>arr2[j][k];
		
		a1--;
		a2--;
		
		for(int j = 0 ; j < 4 ; j++)
			for(int k = 0 ; k < 4 ; k++){
				if(arr1[a1][j] == arr2[a2][k]){
					ans1++;
					ans2 = arr1[a1][j];	
				} 
			}
		//cout<<"ans2 = "<<ans2<<endl;
		//cout<<"ans1 = "<<ans1<<endl;
		
		out<<"Case #"<<i+1<<": ";
		if(ans1 == 1) out<<ans2;
		else if(ans1 == 0) out<<"Volunteer cheated!";
		else out<<"Bad magician!";
		out<<endl;
	}
	
	
	in.close();
    out.close();
	
	return 0;
}
