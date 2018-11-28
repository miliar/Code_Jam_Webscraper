#include <iostream>
#include <string>

using namespace std;

int main()
{
    bool flag[10];
    string stringN;
    int T, N, i=1, flagFinal=0, newN;
    cin>>T;
    for(int z=0; z<T; z++){
        cin>>N;
        for(int p=0; p<10; p++)
            flag[p] = 0;
       if(N == 0)
    	stringN = "Insomnia";
    	else{
	        while(!flagFinal){
	            newN = i*N;
	            stringN = to_string(newN);
	            for(int j=0; j<stringN.length(); j++){
	                if(stringN[j] == '0'){
	                    flag[0] = 1;
	                }
	                else if(stringN[j] == '1'){
	                    flag[1] = 1;
	                }
	                else if(stringN[j] == '2')
	                    flag[2] = 1;
	                else if(stringN[j] == '3')
	                    flag[3] = 1;
	                else if(stringN[j] == '4')
	                    flag[4] = 1;
	                else if(stringN[j] == '5')
	                    flag[5] = 1;
	                else if(stringN[j] == '6')
	                    flag[6] = 1;
	                else if(stringN[j] == '7')
	                    flag[7] = 1;
	                else if(stringN[j] == '8')
	                    flag[8] = 1;
	                else if(stringN[j] == '9')
	                    flag[9] = 1;
	            }
	            if(flag[0] & flag[1] & flag[2] & flag[3] & flag[4] & flag[5] & flag[6] & flag[7] & flag[8] & flag[9])
	            	flagFinal = 1;
	            i++;
	        }
    	}
        cout<<"Case #"<<z+1<<": "<<stringN<<endl;
        flagFinal = 0;
        i=1;
    }
    return 0;
}
