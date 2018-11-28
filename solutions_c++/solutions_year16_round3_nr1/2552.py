#include <iostream>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

main(){
    
    int TestCases;
    cin >> TestCases;
    
    for(int tc=1; tc<=TestCases; tc++){
        int noOfParties,temp,sum=0;
        std::vector<int> senators;
        
        string anwser;
        
        cin >> noOfParties;
        
        for (int i = 0;i<noOfParties;i++){
            cin >> temp;
            sum+=temp;
            senators.push_back(temp);
        }
        
        while(sum){
            auto max = std::max_element(senators.begin(),senators.end());
            auto dist = std::distance(senators.begin(), max);
            
            const char c = dist+65;
            string a(1,c);
            
            anwser.append(a);
            //max--;
            senators[dist]--;
            sum-=1;
            
            
        if(sum){
                auto max = std::max_element(senators.begin(),senators.end());
                double power = double(*max)/double(sum);

                if(power> 0.5) continue;
                
                anwser.append(" ");
            
            }
        }
        
       /* for (auto i : senators)
            cout << i << " ";*/
        
        cout << "Case #"<<tc<<": "<<anwser;
        if(tc!=TestCases)cout<<endl;
    }
    
    return 0;
}