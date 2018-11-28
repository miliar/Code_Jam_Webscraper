#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<fstream>

using namespace std;

int main(){

	//FILE *read=fopen("C.in","r");
	//FILE *write=fopen("C_answer.txt","w");

	ifstream read;
	read.open("A.in");

	ofstream write;
	write.open("A_answer.txt");

	int t;
	//fscanf(read,"%d",&t);
	read>>t;

	for(int i=0;i<t;i++){
		int n;
		read>>n;

		vector<int> p(n);
		int sum=0;
		for(int j=0;j<n;j++){
			read>>p[j];
			sum+=p[j];
		}

		write<<"Case #"<<i+1<<": ";

		int idx1=0;
		//int count=0;
		do{
			idx1=0;
		
			for(int j=1;j<n;j++){
				if(p[j]>p[idx1])idx1=j;
			}

			//
			bool single=true;
			float val1 = (float)sum-1;
			for(int j=0;j<n;j++){
				if(j==idx1)continue;

				if((float)p[j]/val1 > 0.5)single=false;

			}


			write<<(char)(idx1+'A');
			sum--;
			p[idx1]--;

			

			if(single){
				write<<" ";
			}/*else{
				count++;
				//if(count==2)write<<" ";
			}*/

		}while(sum!=0);

		write<<endl;
	}

	//getchar();

	//fclose(read);
	//fclose(write);

	read.close();
	write.close();

	return 0;
}