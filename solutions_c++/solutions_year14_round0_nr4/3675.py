# include <iostream>
#include <algorithm>

using namespace std;

int main(){

  int T=0, N=0;
  cin>>T;
//cout<<"\n T  == "<<T;
  for(int cases=1; cases<=T ; ++cases)
  {


    cin>>N;
//cout<<"\n  N  ==  "<<N;

    float Naomi[N], Ken[N];

    for(int i=0; i<N ; ++i)
    {
        cin >> Naomi[i];
    }
    for(int i=0; i<N ; ++i)
    {
        cin>> Ken[i];
    }
    sort(Naomi, Naomi+N);
    sort(Ken, Ken+N);



/*
for(int i=0; i<N ; ++i)
    {
        cout <<" "<< Naomi[i];
    }
    cout<<"\n";
    for(int i=0; i<N ; ++i)
    {
        cout <<" "<< Ken[i];
    }
    cout<<"\n";
*/
int scoreNO=0, scoreND=0, naomistart= 0, kenstart=0, naomiend=N-1, kenend=N-1;


/////////////////////////    optimal score   ////////////////

while( naomiend >= naomistart)
    {

//cout<<"\n in while start";
        if (Naomi[naomiend] > Ken[kenend])
        {
            ++scoreNO;
            ++kenstart;
            --naomiend;



        }else
        {
            //++scoreN;
            --naomiend;

            --kenend;

        }
    }



 //cout<<"\n  putting score optimal :  "<<scoreNO  ; //<<"    "<<scoreK <<"\n";



scoreND=0, naomistart= 0, kenstart=0, naomiend=N-1, kenend=N-1;

//int truth=1;
while( naomistart <= naomiend)
    {

//cout<<"\n in while start";

        if (Naomi[naomiend] < Ken[kenend])
        {
//cout<<"\n  "<<" NAOMI :  "<< Naomi[naomiend] <<"   "<<"  ken :  "<<Ken[kenend];
         ++naomistart;
         --kenend;

        }else{

            ++scoreND;
            --naomiend;
            --kenend;

        }

    }

cout <<"Case #"<<cases <<": "<<scoreND<<" "<<scoreNO<< "\n";// score Deceptive  :  " <<scoreND <<"\n";

 ////////////////////////        deceptive score    /////////////////
/*
 scoreND=0; Naomistart= 0; kenstart=0; naomiend=N-1; kenend=N-1;

int fault=1;

while(Naomistart !<= naomiend){
//while( fault && kenend>= 0 )
{

if(Naomi[Naomistart] > ken[kenend]){ scoreND += naomiend - Naomistart; }

    else if(Naomi[Naomistart] < Ken[kenstart]){
    ++Naomistart;
    --kenend;
    //--scoreND;
    }else if

// cout<<("\n hungu fafa");
}
}


 cout<<"Case #"<<cases<<": "<<scoreND<<" "<<scoreNO<<"\n" ; //<<"    "<<scoreK <<"\n";





  }
*/

}
return 0;
}




