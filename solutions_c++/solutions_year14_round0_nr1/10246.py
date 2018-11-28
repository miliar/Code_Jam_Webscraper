#include <iostream>
#include <algorithm>   
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    int k = 0;
    while (t--){
        k++;
        int a[2];
        cin >> a[0];
        int x[4][4], y[4][4];
        for(int i =0 ; i<4 ; i++){
            for (int j = 0 ; j<4 ; j++){
                cin >> x[i][j];
            }
        }
        cin >> a[1];
        for(int i =0 ; i<4 ; i++){
            for (int j = 0 ; j<4 ; j++){
                cin >> y[i][j];
            }
        }
        int first[4] ;
        for ( int i = 0 ; i< 4 ; i ++){
		    first[i]= x[a[0]-1][i];
	    }
	
	    int second[4];
	    for ( int i = 0 ; i< 4 ; i ++){
		    second[i] = y[a[1]-1][i];
	    }
        std::vector<int> v(8); 
        std::vector<int>::iterator it;

	std::sort (first,first+4); 
	std::sort (second,second+4);

	it=std::set_intersection (first, first+4, second, second+4, v.begin());
	                                           
	v.resize(it-v.begin());                    
    int size = v.size();
    if(size == 1){
        cout << "Case #" << (k) << ": " << v[0] << endl; 
    } else if (size > 1){
        cout << "Case #" << (k) << ": Bad magician!" <<  endl;     
    } else if (size == 0) {
        cout << "Case #" << (k) << ": Volunteer cheated!" << endl; 
    }
        
    }
    return 0;
}
