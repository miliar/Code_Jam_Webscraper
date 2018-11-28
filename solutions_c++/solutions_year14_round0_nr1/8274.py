#include<iostream>
 using namespace std;
 int main()
 {
	 int t;
	 int A[10][10];
	 int row1; int row2;
	 int B[10][10];
	 int M[10];
	 int N[10];
	 int save=0;
	 
	 cin >> t;
	 int x=1;
	 while(t!=0)
	 {
		 
		 cin>>row1;
		 for (int i=0; i<4; i++)
		 {
			 for (int j=0; j<4; j++)
			 {
				 cin>> A[i][j];
			 }
		 }
		 
		
		 cin>>row2;
		
		 for (int i=0; i<4; i++)
		 {
			 for (int j=0; j<4; j++)
			 {
				 cin>> B[i][j];
			 }
		 }
		 
		 for (int i=0; i<4; i++)
		 {
			 M[i]=A[row1-1][i];
		 }
		 for(int i=0; i<4; i++)
		 {
			 N[i]=B[row2-1][i];
		 }
		 int count=0;
		 for(int i=0; i<4; i++)
		 {
			 for (int j=0; j<4; j++)
			 {
				 if (M[i]==N[j])
				 {
					 save=M[i];
					 count++;
				 }
			 }
		 }
			
		 
		 if (count==1)
		 {
			 cout<<"Case #"<<x<<": "<<save<<endl;
		 }
		 else if (count==0)
		 {
			 cout<<"Case #"<<x<<": Volunteer cheated! "<<endl;
		 }
		 else if (count >1)
		 {
			 cout<<"Case #"<<x<<": Bad magician! " <<endl;
		 }

		 x++;
		 t--;
	 }
}
