#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{


    
    
    
    
    int total;
    cin >> total;
    
    for(int i=0;i<total;i++){
        
        int size;
        cin >> size;
        
        vector<double> list1;
        vector<double> list2;
            
        for(int j=0;j<size;j++){
            
            double temp;
            cin >> temp;
            list1.push_back(temp);
            
            
        }   
        
        for(int j=0;j<size;j++){

            double temp;
            cin >> temp;
            list2.push_back(temp);

            
        }   
    
    
        
        sort(list1.begin(), list1.end());
        sort(list2.begin(), list2.end());
    
    
        vector<double> templist2;
        
        for(int j=0;j<list2.size();j++){
            templist2.push_back(list2[j]);
        }
    
    
        
        int count = 0;
        
        for(int j=0;j<list1.size();j++){
    
            for(int k=0;k<list2.size();k++){
    
                if(list1[j] > list2[k]){
                    count++;
                    list2[k]= 5.0;
                    break;
                }                
                
            }
            
            
        }
        
        
        
        int score1 = count;
        
        
        
            
        int score = 0;
        
        int front_index = 0;
        int end_index = templist2.size()-1;
        
        
        for(int j=(list1.size()-1); j>=0; j--){
            
            
            if(list1[j] > templist2[end_index]){
                score++;
            }
            else
            {
                end_index--;
                
            }
            
        }
        
        
        
        cout << "Case #" << i+1 << ": " << score1 << " " << score <<  endl;
        
        
            
        
        
        
    }
    
    
    
    
    


   return 0;
}
