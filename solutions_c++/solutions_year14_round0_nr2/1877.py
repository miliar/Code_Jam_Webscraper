#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string.h>
using namespace std;
int main(){
    int test_cases;
    freopen("g:/input.txt","r",stdin);
    freopen("g:/output.txt","w",stdout);

    cin>>test_cases;
    double C,F,X;
    for(int caseNum=0;caseNum<test_cases;caseNum++){
        cin>>C;
        cin>>F;
        cin>>X;
        double passedTime=0;
        double currentProductionRate=2;
        double timeRequired=X/2;
        double timeRequiredWithExtraFarm=(X/(F+2))+C/2;
        while(timeRequiredWithExtraFarm<timeRequired)
        {
            timeRequired=timeRequiredWithExtraFarm;
            passedTime+=(C/currentProductionRate);
            currentProductionRate+=F;
            timeRequiredWithExtraFarm=passedTime+(C/currentProductionRate)+(X/(currentProductionRate+F));

        }
      cout<<"Case #"<<caseNum+1<<": ";
      printf("%.7lf",  timeRequired);
      cout<<endl;
    }
    return 0;
    }

