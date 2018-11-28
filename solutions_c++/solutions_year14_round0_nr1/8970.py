    #include <sstream>
    #include <string>
    #include <vector>
    #include <stdlib.h>
    #include <iostream>
    #include <fstream>
    #include <algorithm>
    #include <iterator>
 
 std::vector<int> Calc_Intersection (std::vector<int> &v1, std::vector<int> &v2, int L) {
    
 //   std::cout<<"Calculating "<<std::endl;
    
    std::vector<int> v3;
    
    std::vector<int>::iterator it3;
       std::vector<int>::iterator it2;
       std::vector<int>::iterator it1;
   
   //     std::cout<<"Ignazio 1 "<<std::endl;
        
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    
  //       std::cout << "Sort_vec 1 is ";
  //  for (it1=v1.begin(); it1!=v1.end(); ++it1)
  //  std::cout << ' ' << *it1<<std::endl;
    
    //     std::cout << "Sort_vec 2 is ";
   // for (it2=v2.begin(); it2!=v2.end(); ++it2)
   // std::cout << ' ' << *it2<<std::endl;
    
  // std::cout<<"Ignazio 2"<<std::endl;
    
  std::set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),back_inserter(v3));
  
  //      std::cout<<"Ignazio 3"<<std::endl;
   //  it=std::set_intersection (v1.begin(), v1.end(), second, second+5, v.begin());
  
//   v3.resize(v3.begin());
  
   std::cout<<"Case #"<<L<<": ";
  
//    for (it3=v3.begin(); it3!=v3.end(); ++it3)
 //   std::cout << ' ' << *it3;
  
   if (v3.empty())
   {
    std::cout<<"Volunteer cheated!"<<std::endl;
   } else if(v3.size()==1) {
             std::cout<<v3[0]<<std::endl;
                           } else { std::cout<<"Bad magician!"<<std::endl;
                                }
                                
    
    return v3;
}


    
    int main () {
        
        
    int num_case=0;
    std::string line;
    std::vector<int> vec1;
    std::vector<int> vec2;
    std::vector<int> vec3;
    int i,n;
    int first_row=0;
    int second_row=0;
    
         std::vector<int>::iterator it1;
        std::vector<int>::iterator it2;
    

    std::ifstream infile("A-small-attempt0.in");
    std::getline(infile,line);
    std::stringstream ss(line);
    ss>>num_case;
 //   std::cout << "Num case is :"<< num_case<<std::endl;
    
      for (int l=0;l<num_case;l++){
    //     std::cout << "L is :"<< l<<std::endl;
        std::getline(infile,line);
        std::stringstream st(line);
        st>>first_row;
        
             for (int k=1;k<5;k++){
        //        std::cout << "K 1 is :"<< k <<std::endl;
            std::getline(infile,line);
            if (k==first_row) {
            std::stringstream st(line);
            while(st >> i) //Extract integers from line
            vec1.push_back(i);
            }
            //  std::cout<<"Vec 1 is :";
 //   for (it1=vec1.begin(); it1!=vec1.end(); ++it1)
 //   std::cout<< ' ' << *it1;
 //   std::cout<<std::endl;
           // V1.push_back(vec);
            
           // vec.clear();
             }
             
        std::getline(infile,line);
        std::stringstream sv(line);
        sv>>second_row;
      //  std::cout << "second_row is :"<< second_row <<std::endl;
        
            for (int k=1;k<5;k++){
           //     std::cout << "K 2 is :"<< k <<std::endl;
            std::getline(infile,line);
            if (k==second_row) {
            std::stringstream su(line);
            while(su >> n) //Extract integers from line
            vec2.push_back(n);
            }
                //          std::cout<<"Vec 2 is :";
              //  for (it2=vec2.begin(); it2!=vec2.end(); ++it2)
              //        std::cout<< ' ' << *it2;
              //          std::cout<<std::endl;
          //  V2.push_back(vec);
           // vec.clear();
             }

             Calc_Intersection(vec1,vec2,l+1);
  
             vec1.clear();
             vec2.clear();
        
        
      }
    return 0;
    
    }