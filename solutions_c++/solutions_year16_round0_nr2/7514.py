#include <iostream>
#include<string>

using namespace std;

string replaceChar(string str) {
  for (int i = 0; i < str.length(); ++i) {
    if (str[i] == '+')
      str[i] = '-';
    else
	str[i] = '+';
  }

  return str;
}

string revStr(string str){
    string str1 = "";
    for(int i=str.length()-1;i>=0;i--){
        str1+=str[i];
    }
    return str1;
}


int main()
{
    string str,str1, firstHalf, secondHalf,firstHalf1, secondHalf1;
    int t,set,set1,round,j,k;
    cin>>t;

    for(int i=1;i<=t;i++){
            round = 0;
            cin>>str;
            str1="";

            for(int p=0;p<str.length();p++){
                    str1 += "+";
            }

            while(str.compare(str1)!=0)
            {
                for(j = str.length()-1;j>=0;j--){
                        if(str[j]=='-')break;
                }
                set = j+1;

                if(j >= 0){

                    if(set == str.length()){
                        firstHalf = str;
                        secondHalf = "";
                    } else{
                        firstHalf = str.substr(0,set);
                        secondHalf = str.substr(set);
                    }


                    for(k=0;k<firstHalf.length();k++){
                            if(str[k]=='-')break;
                    }

                    if(k>0){
                        firstHalf1 = firstHalf.substr(0,k);
                        secondHalf1 = firstHalf.substr(k);
                        firstHalf1 = replaceChar(revStr(firstHalf1));
                        firstHalf1 += secondHalf1;
                        firstHalf = firstHalf1;
                        round++;
                    }



                    firstHalf = replaceChar(revStr(firstHalf));
                    firstHalf += secondHalf;
                    round++;
                }

                str = firstHalf;
            }

            cout<<"Case #"<<i<<": "<<round<<"\n";
    }
    return 0;
}

