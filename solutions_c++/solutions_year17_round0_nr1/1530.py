#include<bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;

	string s,sl,sr;
	 long long int n,k,ansl,ansr,i,j;

	for (int test = 1; test <= t; ++test)
	{
        ansl=0;ansr=0;
        cin>>s;
        cin>>k;
        sl=s;
        sr=s;
        for( i=0;i<=sl.length()-k;i++){

            if(sl[i]=='-'){

                for( j=i;j<i+k;j++ ){
                    if(sl[j]=='+'){sl[j]='-';}
                    else{sl[j]='+';}
                }
                ansl++;
            }


        }

        for( i=sl.length()-k+1;i<sl.length();i++){

            if(sl[i]=='-'){
                ansl=-1;break;
            }

        }

        for( i=sr.length()-1;i>=k-1;i--){

            if(sr[i]=='-'){

                for( j=i;j>=i-k+1;j-- ){
                    if(sr[j]=='+'){sr[j]='-';}
                    else{sr[j]='+';}
                    //cout<<j;
                    if(j==0){break;}
                    //cout<<s[j];
                }

                ansr++;//cout<<endl;
            }
        //cout<<i<<" "<<sr;
        }

        for(int i=k-2;i>=0;i--){

            if(sr[i]=='-'){
                ansr=-1;break;
            }

        }

   //     cout<<ansl<<" "<<ansr<<endl;

        if(ansl==-1 &&ansr>=0){
        cout<<"Case #"<<test<<": "<<ansr<<endl;
        }
        else if(ansl==-1 &&ansr==-1){
        cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
        }
       else if(ansl>=0 &&ansr==-1){
        cout<<"Case #"<<test<<": "<<ansl<<endl;
        }
        else if(ansl>=0 &&ansr>=0){
        cout<<"Case #"<<test<<": "<<min(ansl,ansr)<<endl;
        }



	}


	return 0;
}
