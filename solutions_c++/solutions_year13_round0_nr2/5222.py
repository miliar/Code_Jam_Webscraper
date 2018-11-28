//
//  main.cpp
//  round1_2
//
//  Created by Mac on 13. 4. 13..
//  Copyright (c) 2013년 jwh. All rights reserved.
//

#include <iostream>

bool check_hv(int _n, int _i, int* _map, int _step) {
    int _dot = *_map;
    
    int _v = _i;
    int* _map_ptr = _map;
    while (_v >= 0) {
        if(*_map_ptr > _dot)
            return false;
        _map_ptr-=_step;
        _v--;
    }
    
    _v = _i;
    _map_ptr = _map;
    while (_v < _n) {
        if(*_map_ptr > _dot)
            return false;
        _map_ptr+=_step;
        _v++;
    }
    return true;
}

bool check_dot(int _w, int _h, int _x, int _y, int* _map) {
    return check_hv(_h, _y, _map, _w) || check_hv(_w, _x, _map, 1);
}

bool check_line(int _w, int _h, int _x, int _y, int* _map, bool _is_x) {
    int len = _is_x ? _w : _h;
    int step = _is_x ? 1 : _w;
    int i = 0;
    while (i < len) {
        if(!check_dot(_w, _h, _is_x ? i : _x, _is_x ? _y : i, _map))
            return false;
        _map += step;
        i++;
    }
    return true;
}

bool check(int _w, int _h, int* _map) {
    int* ptr = _map;
    for(int i = 0; i < _h; i++) {
        if(!check_line(_w, _h, 0, i, ptr, true))
            return false;
        ptr+=_w;
    }
    ptr = _map;
    for(int i = 0; i < _w; i++) {
        if(!check_line(_w, _h, i, 0, ptr, false))
            return false;
        ptr++;
    }
    return true;
}

int main(int argc, const char * argv[])
{
    FILE* f = fopen(argv[1], "r");
    int len;
    fscanf(f, "%d", &len);
    fseek(f, SEEK_CUR, 1);
    for (int i = 0; i < len; i++) {
        int w, h;
        fscanf(f, "%d %d", &h, &w);
        fseek(f, SEEK_CUR, 1);
        int* map = (int*)malloc(sizeof(int) * w * h);
        int* ptr = map;
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                fscanf(f, "%d", ptr);
                fseek(f, SEEK_CUR, 1);
                ptr++;
            }
        }
        bool success = check(w, h, map);
        printf("Case #%i: %s\n", i+1, success ? "YES" : "NO");
        free(map);
    }
    return 0;
}

