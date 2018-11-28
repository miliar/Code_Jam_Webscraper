#include<stdio.h>
#include<vector>
using namespace std;
int calc_time(vector<int> &num_pan){
    int max_pan = 0;
    for(int i= 0 ; i < num_pan.size();i++){
        if(num_pan[i] > max_pan) max_pan = num_pan[i];
    }
    return max_pan;
}
int main(){
    int T;scanf("%d",&T);
    for(int _ = 0 ; _ < T ;_++){
        int n;
        scanf("%d", &n);
        vector<int> pan_cnt(n,0);
        int max_pan =0;
        for(int i = 0; i < n ; i++){
            int x; scanf("%d",&x); pan_cnt[i] = x;
            max_pan = max_pan < x ? x : max_pan;
        }
        vector<int> num_pan(max_pan+1,0);
        for(int i = 0; i < n ; i++){
            num_pan[pan_cnt[i]]++;
        }
        int ans = 0;
        while(true){
            int min_time = max_pan;
            int next_max_pan = max_pan;
            int min_sleep = 0;
            vector<int> next_num_pan = num_pan;
            for(int target = 1 ; target < max_pan ; target++){
                vector<int> tmp_pan = num_pan;
                int cnt_sleep = 0;
                for(int cur = max_pan ; cur > target ; cur--){
                    if(tmp_pan[cur] > 0){
                        //cnt_sleep += tmp_pan[cur];

                        int best_divcnt = -1;
                        for(int div_cnt = 2 ; div_cnt <= cur ; div_cnt++){
                            int div = cur/div_cnt;
                            int mod = cur%div_cnt;
                            int eat = div + (mod > 0);
                            if(eat > target) continue;
                            best_divcnt = div_cnt;
                            break;
                        }
                        //printf("cur = %d bs = %d\n",cur, best_divcnt);
                        tmp_pan[cur/best_divcnt]+= (best_divcnt - cur%best_divcnt)*tmp_pan[cur];
                        tmp_pan[cur/best_divcnt+1] += (cur%best_divcnt)*tmp_pan[cur];

                        cnt_sleep += (best_divcnt-1)*tmp_pan[cur];
                        tmp_pan[cur] = 0;
                    }
                }
                if(cnt_sleep + target < min_time){
                    min_time = cnt_sleep + target;
                    next_max_pan = target;
                    next_num_pan = tmp_pan;
                    min_sleep = cnt_sleep;
                }
            }
            if(min_time == max_pan){
                break;
            }
            max_pan = next_max_pan;
            num_pan = next_num_pan;
            ans += min_sleep;
        }
        printf("Case #%d: %d\n",_+1, ans + max_pan);
    }
    return 0;
}
