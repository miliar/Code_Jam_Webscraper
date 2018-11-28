#include<iostream>

using namespace std;
int main(){
	int cases,counter=0;
	cin>>cases;
	while(cases--){
		counter++;
		int correctV,correctH,ver[4],hor[4],deck[4][4];
		cin>>correctV;
		for(int i=0;i<4;i++){
			cin>>deck[i][0]>>deck[i][1]>>deck[i][2]>>deck[i][3];
			if(i==(correctV-1)){

				ver[0]=deck[i][0];
				ver[1]=deck[i][1];
				ver[2]=deck[i][2];
				ver[3]=deck[i][3];
			}
		}

		cin>>correctH;
		for(int i=0;i<4;i++){
                        cin>>deck[i][0]>>deck[i][1]>>deck[i][2]>>deck[i][3];
                        if(i==(correctH-1)){  

                                hor[0]=deck[i][0];
                                hor[1]=deck[i][1];
                                hor[2]=deck[i][2];
                                hor[3]=deck[i][3];
                        }                    
                }
		int matches=0,mValue;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(ver[i]==hor[j]){
					matches++;
					mValue=ver[i];
					break;
				}
			}
		}
		if(matches==0){
			cout<<"Case #"<<counter<<": Volunteer cheated!"<<endl;
		} 
		else if(matches ==1){
			cout<<"Case #"<<counter<<": "<<mValue<<endl;
		}
		else{
			cout<<"Case #"<<counter<<": Bad magician!"<<endl;
		}

	}
	return 0;
}
