#include <bits/stdc++.h>


char str[105];
int main(){
//    #ifndef ONLINE_JUDGE
//	freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
//    #endif
    int T, cas = 1;
    scanf ("%d", &T);
    while (T--){
        scanf("%s", str);
		int len = strlen(str);
        std::vector <int> sub;
        std::vector <int> add;
        bool flag = true;
        for (int i = len-1; i >= 0; ){
            if (str[i] == '+' && flag){
				i--;
                continue;
            }else{
				flag = false;
                bool ok = false;
                while (i >= 0 && str[i] == '-'){
					if (!ok){
						sub.push_back(i);
						ok = true;
					}
					i--;
                }
                ok = false;
				while (i >= 0 && str[i] == '+'){
					if (!ok){
						add.push_back(i);
						ok = true;
					}
					i--;
                }
            }
        }
        int ans = 0;
        if(sub.size() == 0){
			ans = 0;
        }else if (add.size() == 0){
			ans = 1;
        }else{
            if (add[add.size()-1] > sub[sub.size()-1]){
                ans = sub.size() * 2 - 1;
            }else{
				ans = sub.size() * 2;
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
