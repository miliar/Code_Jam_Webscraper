/*************************************************************************
	> File Name: problemB.sourcecode.cpp
	> Author: 
	> Mail: 
	> Created Time: Sat Apr 11 18:50:53 2015
 ************************************************************************/

int special_time(int cake_count, int allowed_max_count) {
    return (cake_count - 1) / allowed_max_count;
}


int solve(vector<int> cakes, int max_cake) {
    int min_time = INT_MAX;
    for (int test = 1; test <= max_cake; ++test) {
        int each_time = 0;
        for (int i = 0; i < cakes.size(); ++i) {
            each_time += special_time(cakes[i], test);
        }
        each_time += test;
        if (each_time < min_time) {
            min_time = each_time;
        }
    }
    return min_time;
}


int main () {
    freopen("/Users/feliciafay/Downloads/B-small-attempt1.in","r",stdin);
    int test_number = 0;
    cin>>test_number;
    int number;
    int each_cake;
    string cakes;
    int count = 1;
    while (cin>>number) {
        vector<int> cakes_vector;
        int max_cake = 0;
        for(int i = 0; i < number; ++i) {
            cin>>each_cake;
            cakes_vector.push_back(each_cake);
            if (each_cake > max_cake) {
                max_cake = each_cake;
            }
        }
//        for (int i = 0; i < cakes_vector.size(); ++i) {
//            std::cout<<cakes_vector[i]<<",\t";
//        }
//        std::cout<<std::endl;
        int min_time = solve(cakes_vector, max_cake);
        printf("Case #%d: %d\n", count, min_time);
        ++count;
    }
}

