#include <iostream>
#include <string>

using namespace std;

main(){
    
    int TestCases;
    cin >> TestCases;
    
    for(int tc=1; tc<=TestCases; tc++){
        std::string input;
        cin >> input;
    
        int flips = 0;
        char currentSide = '+';
  for (std::string::reverse_iterator rit=input.rbegin(); rit!=input.rend(); ++rit){
      if(*rit!=currentSide){
          flips++;
          currentSide=*rit;
    }
}
    
        
        cout << "Case #"<<tc<<": "<<flips;
        if(tc!=TestCases)cout<<endl;
    }
    
    return 0;
}