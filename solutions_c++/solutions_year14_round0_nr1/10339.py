#include<iostream>
#include<fstream>
#include<sstream>
#include<string>

using namespace std;

int main(){
	stringstream ss;

	ifstream in("inp.in");
	ofstream out("out.out");

	int test,c = 1;
	char nxt[10];
	in>>test;
	
	in.getline(nxt, 10);
	while(test-->0){
		//cout<<test<<endl<<endl;
		// in every case there will be two arrays to be input. Function or just good old fashioned hard code? :D
		int choice1=0, choice2=0, i, j, arr1[4][4],arr2[4][4];
		int line1[4], line2[4];
		
		
		in>>choice1;
		
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				in>>arr1[i][j];
			}
			}


		for(i=0;i<4;i++)
			line1[i] = arr1[choice1-1][i];

		//choice 2
		
		in>>choice2;
		
		//in.getline(nxt, 10); // just to get it to next line apparently.
							 // comment this line out first if debugging is required.
		
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				in>>arr2[i][j];
		}
		for(i=0;i<4;i++)
			line2[i] = arr2[choice2-1][i];

		//cout<<choice1<<"    "<<choice2<<endl;
		

		//LOGIC: if no common elements, volunteer cheated
		//		 if 1 common element, ouput
		//		 if more than 1 common element, BAD Magician!

		int counter=0, result=0;

		for (i=0;i<4;i++){
			
			for(j=0;j<4;j++){
				
				if ( line1[i] == line2[j]){
					counter++;
					result = line2[j];
				}

			}
		}


		ss<<"Case #";
		ss<<c++;
		ss<<": ";

		if (counter == 0)
			ss<<"Volunteer cheated!\n";
		else if(counter == 1){
			ss<<result;
			ss<<"\n";
		}
		else{
			ss<<"Bad Magician!\n";
		}
		//OUTPUT RESULT TOO
	}
	out<<ss.str();
	in.close();
	out.close();
	//system("PAUSE");		comment it out before submiting
	return 0;

}