#include<iostream>
#include<vector>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int case_i=0; case_i<t;case_i++){
        int d, minutes=0;
        vector<int> num_diners;
        cin >> d;
        for(int j=0; j<d;j++){
            int pi;
            cin >> pi;
            if(pi>num_diners.size()){
                num_diners.resize(pi);
            }
            num_diners[pi-1]++;
        }
        int ik = num_diners.size()-1;
        while(ik >= 0){
            int dividemax = ik-1;
//            int shift = ik-dividemax;
//            int elements_inside = 0;
//            for(int i=ik; i>=0 && i>dividemax;i--)
//                elements_inside += num_diners[i];
//            int max_diff = shift-elements_inside;
            int max_diff = 0;
            for(int i=dividemax; i>=0;i--){
                int timeautoshift=ik-i;
                int timetoshiftall=0;
                int autoshifts=0;
                for(int j=ik; j>=0 && j-autoshifts>i;j--)
                    if(num_diners[j]>0)
                    {
                        int timetoshift = (j-autoshifts)/(i+1);
                        timetoshift *= num_diners[j];
                        if(timetoshift >= j-i-autoshifts){
                            timetoshift = j-i-autoshifts;
                            autoshifts += timetoshift;
                        }
                        timetoshiftall+=timetoshift;
                    }
                int diff_aux = timeautoshift - timetoshiftall;
                if( diff_aux > max_diff){
//                    cout << "BestChoice index "<<dividemax << "->"<<i <<": "<<max_diff<< "->"<<diff_aux<<endl;
                    dividemax = i;
                    max_diff = diff_aux;
                }
            }
            if(max_diff>0){
//                cout << "Moving "<<ik <<"->"<<dividemax<<endl;
                num_diners[ik]--;
                num_diners[dividemax]++;
                num_diners[ik-dividemax-1]++;
                if(num_diners[ik] == 0){
                    while(num_diners[ik] == 0)ik--;
                    num_diners.resize(ik+1);
                }
                minutes++;
            }
            else{
                minutes += ik+1;
                ik = -1;
            }
        }
        cout << "Case #" <<(case_i+1) << ": "<<minutes<<endl;
    }
    return 0;
}
