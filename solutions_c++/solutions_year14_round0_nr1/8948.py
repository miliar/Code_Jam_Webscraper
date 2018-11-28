#include<iostream>
#include<fstream>
using namespace std;
int main(){
	
    int array[4][4];
    int arr[8];
	int a, b, c, d, k, z;
	ifstream myfile ("A-small-attempt6.in");
	ofstream myfile2 ("file2.txt");
    myfile >> a;
	for(int i=0;i<a;i++){
		z=0, k=0;
    	myfile >> b;
    	//cout << "B = " << b << endl;
    	//cout << "Case #"<<(i+1)<<": ";
   		myfile2<< "Case #"<<(i+1)<<": ";
    	for(int i=0;i<4;i++){
    		for(int j=0;j<4;j++){
    			myfile >> array[i][j];
    		}
    	}
    	
     	/*for(int i=0;i<4;i++){
    		for(int j=0;j<4;j++){
    			cout << array[i][j]<<" ";
    		}
    		cout << endl;
    	}*/


    	for(int i=0;i<4;i++){
    		arr[k] = array[b-1][i];
    		k++;
    	}
    	
    	myfile >> c;
	   	//cout << "C = " << c << endl;
	   	
    	for(int i=0;i<4;i++){
    		for(int j=0;j<4;j++){
    			myfile >> array[i][j];
    		}
    	}

    	/*for(int i=0;i<4;i++){
    		for(int j=0;j<4;j++){
    			cout << array[i][j]<<" ";
    		}
    		cout << endl;
    	}*/

		k=4;
		for(int i=0;i<4;i++){
    		arr[k] = array[c-1][i];
    		k++;
    	}
    	
    	for(int i=0;i<7;i++){
    		for(int j=i;j<7;j++){
				if(arr[i] == arr[j+1]){
					z++;
					d = arr[i];
				}
			}
    	}
    	/*cout<<"Z = "<<z<<endl;
    	cout<<endl<<endl;
    	for(int i=0;i<8;i++){
    		cout << arr[i] << " ";
    	}
    	cout<<endl<<endl;

    	*/
    	if(z>1){
    		myfile2 << "Bad magician!" <<endl;
    		//cout << "Bad magician!" <<endl;
    	}
		else if (z==0){
			myfile2 << "Volunteer cheated!" <<endl;
			//cout << "Volunteer cheated!" <<endl;
		}
    	else{
    		myfile2 << d << endl;
    		//cout << d << endl;
		}
    }
    myfile.close();
    return 0;
}

